from django.conf.urls import url
from django.urls import path, include
from . import views
from django.templatetags.static import static
from hz_BI import settings

urlpatterns = [
    url(r'^test/', views.test, name='test'),

    # url(r'^write/', views.excelToMysql, name='write'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)