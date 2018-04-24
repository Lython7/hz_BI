from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from yotools.models import SMSCode

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RegistApiView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = ProfileSerializer

@csrf_exempt
def resetit(request):
    if request.method == "POST":
        # print(1)
        cellphone = request.session.get('cellphone', None)
        code = request.POST.get('code', None)
        passwd = request.POST.get('passwd', None)
        sms = SMSCode.objects.get(cellphone=cellphone)
        if code == sms.code:
            # 修改密码
            print(cellphone)
            print(passwd)
            print(code)
            print(sms)
        else:
            # 验证码错误  重新输入
            pass
        return HttpResponse('ok了')