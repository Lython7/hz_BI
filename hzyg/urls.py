from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^test/', views.test, name='test'),

    # url(r'^write/', views.excelToMysql, name='write'),
]