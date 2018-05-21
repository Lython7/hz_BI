from django.conf.urls import url
from django.urls import path, include
from . import views
from . import views

urlpatterns = [
    url(r'^income/([0-9]{4})([0-9]{0,2})([0-9]{0,2})([0-9]{0,2})$', views.income, name='income'),
    url(r'^storect/([0-9]{4})([0-9]{0,2})$', views.store_count, name='store_count'),
    url(r'^odstorect/([0-9]{4})([0-9]{0,2})$', views.ordered_store_count, name='ordered_store_count'),
    url(r'^orderct/([0-9]{4})([0-9]{0,2})$', views.order_count, name='order_count'),
    # url(r'^income/', views.income, name='income'),

    # url(r'sendsms/(?P<cellphone>\d{11})$', demo_sms_send.send_sms, name='sendsms'),
]