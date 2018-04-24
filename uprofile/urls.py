from django.conf.urls import url
from django.urls import path, include
from . import views
from dysms_python import demo_sms_send

urlpatterns = [
    url(r'^resetpwd/$', views.resetit, name='resetit'),

    # url(r'sendsms/(?P<cellphone>\d{11})$', demo_sms_send.send_sms, name='sendsms'),
]