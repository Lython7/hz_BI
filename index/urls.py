from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.loginPage),
    url(r'uauth/', views.doLogin, name='uauth'),

]
