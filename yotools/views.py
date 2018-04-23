import sys, json, time, random
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT


# Create your views here.
from django.http import HttpResponse

from uprofile.models import Uprofile


class SMSClient(object):
    SIGN_NAME = "禾中BI"
    TEMPLATE_CODE = "SMS_133035230"
    REGION = "cn-hangzhou"
    PRODUCT_NAME = "Dysmsapi"
    DOMAIN = "dysmsapi.aliyuncs.com"
    ACCESS_KEY_ID = "LTAIYgwU4bAOm6gs"
    ACCESS_KEY_SECRET = "b02Nu9tXhdNZjAYBn61QYnZRonIIFL"
    PRODUCT = "禾中产品销售有限公司"

    acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
    region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)
#
    @classmethod
    def send_sms(cls, cellphone):

        if Uprofile.objects.filter(ucellphone=cellphone).count() == 1:

            # timeflag = str(time.time()).split('.')[0]
            business_id = uuid.uuid1()
            code = str(random.random() * pow(10, 10))[0:6]
            template_param = {'code': code}
            template_param = json.dumps(template_param)

            smsRequest = SendSmsRequest.SendSmsRequest()

            # 申请的短信模板编码,必填
            smsRequest.set_TemplateCode(cls.TEMPLATE_CODE)

            # 短信模板变量参数,友情提示:如果JSON中需要带换行符,请参照标准的JSON协议对换行符的要求,比如短信内容中包含
            # 的情况在JSON中需要表示成,否则会导致JSON在服务端解析失败
            if template_param is not None:
                smsRequest.set_TemplateParam(template_param)

            # 设置业务请求流水号，必填。
            smsRequest.set_OutId(business_id)

            # 短信签名
            smsRequest.set_SignName(cls.SIGN_NAME)

            # 短信发送的号码，必填。支持以逗号分隔的形式进行批量调用，批量上限为1000个手机号码,批量调用相对于单条调用及时性稍有延迟,
            # 验证码类型的短信推荐使用单条调用的方式
            smsRequest.set_PhoneNumbers(cellphone)

            # 发送请求
            smsResponse = cls.acs_client.do_action_with_exception(smsRequest)
            resp = json.loads(smsResponse)
            resp['stutas'] = 1
            # resp['timeflag'] = timeflag
            return resp
            # return HttpResponse('ok')

        # if 'OK' == resp.get('Code'):
        #     SMSCode.objects.update_or_create(phone_number=cellphone, code=code, stutas=1, timeflag=timeflag)
        # return HttpResponse(json.dumps(resp), content_type='application/json')
        #
#     #
#     # @classmethod
#     # def query_send_detail(cls, request, biz_id, phone_number):
#     #     queryRequest = QuerySendDetailsRequest.QuerySendDetailsRequest()
#     #
#     #     # 查询的手机号码
#     #     queryRequest.set_PhoneNumber(phone_number)
#     #
#     #     # 可选 - 流水号
#     #     queryRequest.set_BizId(biz_id)
#     #
#     #     # 必填 - 发送日期 支持30天内记录查询，格式yyyyMMdd
#     #     send_date = datetime.strftime(datetime.today(), '%Y%m%d')
#     #     queryRequest.set_SendDate(send_date)
#     #
#     #     # 必填-当前页码从1开始计数
#     #     queryRequest.set_CurrentPage(1)
#     #
#     #     # 必填-页大小
#     #     queryRequest.set_PageSize(10)
#     #
#     #     queryResponse = cls.ACS_CLIENT.do_action_with_exception(queryRequest)
#     #     resp = json.loads(queryResponse)
#     #     return HttpResponse(json.dumps(resp))
#     #
#     # @classmethod
#     # def verify_code(cls, request):
#     #     phone_number = request.GET.get('phone_number', None)
#     #     if phone_number:
#     #         query = SMSCode.objects.filter(phone_number=phone_number).last()
#     #         status = query.stutas
#     #         resp = {}
#     #         code = query.code
#     #         codefront = request.GET.get('code')
#     #         if code == codefront:
#     #             timeflag = query.timeflag
#     #             timefront = request.GET.get('timeflag')
#     #             if int(timefront) - int(timeflag) <= 300:  # ??????
#     #                 if status == 1:
#     #                     # SMSCode.objects.filter(phone_number=phone_number).update(stutas=2)
#     #                     query.stutas = 2
#     #                     query.save()
#     #                     resp['Code'] = 'OK'
#     #                 else:
#     #                     resp['Code'] = 'used'  # 验证码已使用，请重新获取。
#     #             else:
#     #                 resp['Code'] = 'timeOut'  # 验证码已过期，请重新获取。
#     #
#     #         else:
#     #             resp['Code'] = 'ErrCode'
#     #
#     #     return HttpResponse(json.dumps(resp), content_type='application/json')