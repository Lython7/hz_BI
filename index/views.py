import json

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

from overview.models import Show_overview
from uprofile.models import Uprofile
from yotools.models import SMSCode
from . import models, serializers
# from uprofile.models import Permissions_F1
from permissions.models import *

# from dysms_python import demo_sms_send

# 正式使用

def index(request):
    try:
        if request.user.is_authenticated and Uprofile.objects.get(user=request.user).uposition<100:
            return render(request, 'index/index.html', context={})
        else:
            return HttpResponseRedirect('/login/')
    except:
        return HttpResponseRedirect('/login/')

# # 暂时使用
# def index(request):
#     return render(request, 'index/index.html', context={})

def classifyct(request):
    return render(request, 'index/classifyct.html', context={})

def ranking(request):
    return render(request, 'index/ranking.html', context={})

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
            user = authenticate(username=username,password=password)# 类型为<class 'django.contrib.auth.models.User'>

        except:
            return HttpResponse('wrong account or wrong pwd')
        if user:
            if password == 'qwer1234' or username == 'lz':
                # 该密码为默认密码 进入修改密码页面
                # 发送验证码
                cellphone = Uprofile.objects.get(user=user).ucellphone
                request.session['cellphone'] = cellphone

                # resp = demo_sms_send.send_sms(cellphone)
                # timeflag = resp['timeflag']
                # code = resp['code']
                # print(resp['Code'])
                # if 'OK' == resp.get('Code'):
                #     SMSCode.objects.update_or_create(phone_number=cellphone, code=code, stutas=1, timeflag=timeflag)
                return HttpResponseRedirect("/resetpwd")
            else:
                login(request, user)
                # 将USER相关权限写入session
                try:
                    request.session['settings'] = model_to_dict(Show_overview.objects.get(user=user))
                    request.session['ucellphone'] = Uprofile.objects.get(user=user).ucellphone
                # request.session.set_expiry(60000)
                except:
                    request.session['settings'] = {}
                # print(request.session['settings'])
                uposition = Uprofile.objects.get(user=user).uposition
                if uposition < 100:
                    return HttpResponseRedirect("/")
                elif uposition >= 100:
                    return HttpResponseRedirect("/admin")
        else:
            return HttpResponse('wrong account or wrong pwd')


def resetpwd(request):
    # 重置密码API post地址

    pass


def sendEmail():
    pass


def acc_logout(request):

    logout(request)  # 登出

    return redirect("/uauth/")

