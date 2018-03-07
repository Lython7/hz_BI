from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from . import models, serializers


def loginPage(request):
    return render(request, 'index/login.html', context={})

# @login_required
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index/haha.html', context={})
    else:
        return HttpResponseRedirect('/')

def doLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)  # 类型为<class 'django.contrib.auth.models.User'>

        # print(type(models.Customer.objects.get(name="赵凡")))
        # print(user,type(user))
        if user:
            login(request, user)
            staff = user.is_staff
            if staff == 0:
                return HttpResponseRedirect("/index")
            elif staff == 1:
                return HttpResponseRedirect("/yoback")


    # return render(request, "index/login.html")


def acc_logout(request):

    logout(request)  # 登出

    return redirect("/uauth/")

