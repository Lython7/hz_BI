from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view


# Create your views here.
def login_page(request):
    return render(request, 'index/login.html', context={})

def login_auth(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)  # 类型为<class 'django.contrib.auth.models.User'>

        # print(type(models.Customer.objects.get(name="赵凡")))
        # print(user,type(user))
        if user:
            login(request,user)  # 验证成功之后登录
            return HttpResponse('jaja')

    return render(request, "index/login.html")


# def acc_logout(request):
#
#     logout(request)  # 登出
#
#     return redirect("/login")