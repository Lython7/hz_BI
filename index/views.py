from django.contrib.admin import AdminSite
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
# import requests


# Create your views here.
def loginPage(request):
    return render(request, 'index/login.html', context={})

def doLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username,password=password)  # 类型为<class 'django.contrib.auth.models.User'>

        # print(type(models.Customer.objects.get(name="赵凡")))
        # print(user,type(user))
        if user:
            login(request, user)
            staff = User.objects.get(username=username).is_staff
            if staff == 0:
                return render(request, "index/haha.html")
            elif staff == 1:
                return render(request, "index/jaja.html")


    # return render(request, "index/login.html")


# def acc_logout(request):
#
#     logout(request)  # 登出
#
#     return redirect("/login")