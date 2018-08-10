from django.conf.urls import url
from django.urls import path, include
from . import views
from django.templatetags.static import static
from hz_BI import settings

urlpatterns = [
    url(r'^$', views.yoback, name='yoback'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^checkexcel/', views.checkexcel, name='checkexcel'),

    # url(r'^write/', views.excelToMysql, name='write'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)