import json

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

from uprofile.models import Uprofile
from yotools.models import SMSCode
from . import models, serializers
from yotools.views import SMSClient
from dysms_python import demo_sms_send

# @login_required
def index(request):
    if request.user.is_authenticated and request.user.is_staff == 0:
        return render(request, 'index/haha.html', context={})
    else:
        return HttpResponseRedirect('/login/')

def register(request):
    return render(request, 'index/register.html', context={})

def loginPage(request):
    return render(request, 'index/login.html', context={})

# @login_required
def resetpwdPage(request):
    # print(request.session['cellphone'])
    return render(request, 'index/resetpwd.html', context={})


def doLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = authenticate(username=username,password=password)  # 类型为<class 'django.contrib.auth.models.User'>
        except:
            return JsonResponse({'resuld': 'faild'})
        if user:
            if password == 'qwer1234':
                # 该密码为默认密码 进入修改密码页面
                # 发送验证码
                cellphone = Uprofile.objects.get(user=user).ucellphone
                request.session['cellphone'] = cellphone
                request.session.set_expiry(600)
                resp = demo_sms_send.send_sms(cellphone)
                timeflag = resp['timeflag']
                code = resp['code']
                print(resp['Code'])
                if 'OK' == resp.get('Code'):
                    SMSCode.objects.update_or_create(phone_number=cellphone, code=code, stutas=1, timeflag=timeflag)
                return HttpResponseRedirect("/resetpwd")
            else:
                login(request, user)
                ustatus = Uprofile.objects.get(user=user).ustatus
                if ustatus < 100:
                    return HttpResponseRedirect("/")
                elif ustatus >= 100:
                    return HttpResponseRedirect("/yoback")


def resetpwd(request):
    # 重置密码API post地址

    pass


def sendEmail():
    pass


def acc_logout(request):

    logout(request)  # 登出

    return redirect("/uauth/")

