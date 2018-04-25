from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginPage, name='login'),
    url(r'^uauth/$', views.doLogin, name='uauth'),
    url(r'^resetpwd/$', views.resetpwdPage, name='resetpwd'),

    # url(r'regist/', views.register, name='register'),



    # api


]
