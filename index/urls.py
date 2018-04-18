from django.conf.urls import url
from django.urls import path, include
from . import views
from uprofile.views import RegistApiView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', views.loginPage, name='login'),
    url(r'uauth/', views.doLogin, name='uauth'),
    url(r'regist/', views.register, name='register'),



    # api
    url(r'doRegist/', RegistApiView.as_view(), name='doRegist'),


]
