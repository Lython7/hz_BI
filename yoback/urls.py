from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.yoback, name='upload'),
    url(r'^upload/', views.upload, name='upload'),

    # url(r'^write/', views.excelToMysql, name='write'),
]