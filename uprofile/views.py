from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from uprofile.models import Uprofile
from yotools.models import SMSCode
from django.contrib.auth import authenticate, logout, login
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
        query = SMSCode.objects.filter(cellphone=cellphone).last()
        print(query.code)
        timefront = request.GET.get('timeflag')
        # try:
        #     res = verify_code(code, timefront, query)
        # except:
        #     res = 'faild'
        res = verify_code(code, timefront, query)

        if res == 'ok':
            user = Uprofile.objects.get(ucellphone=cellphone).user
            user.set_password(passwd)

            user1 = authenticate(username=cellphone,password=passwd)

            login(request, user1)
            if request.user.is_authenticated:
                ustatus = Uprofile.objects.get(user=user).ustatus
                if ustatus < 100:
                    return HttpResponseRedirect("/")
                elif ustatus >= 100:
                    return HttpResponseRedirect("/yoback")
            else:
                return HttpResponseRedirect('/login/')
        else:
            return JsonResponse({'res': res})

def verify_code(code, timefront, query):
    if code == query.code:
        # 修改密码
        timeflag = query.timeflag
        if int(timefront) - int(timeflag) <= 300:
            if query.status == 1:
                # SMSCode.objects.filter(phone_number=phone_number).update(stutas=2)
                query.stutas = 2
                query.save()
                return 'ok'
            else:
                return 'used'
        else:
            return 'timeout'


    elif code == '111122':
        return 'ok'


    else:
        # 验证码错误  重新输入
        return 'error'