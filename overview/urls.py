from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^incometoday/', views.today_income, name='income_today'), # 今日营收



    # url(r'^sales_amount_month/([0-9]{4})([0-9]{0,2})([0-9]{0,2})([0-9]{0,2})$', views.income_month, name='income_today'), # 销售额
    # url(r'^storect/([0-9]{4})([0-9]{0,2})$', views.store_count, name='store_count'),
    # url(r'^odstorect/([0-9]{4})([0-9]{0,2})$', views.ordered_store_count, name='ordered_store_count'),
    # url(r'^orderct/([0-9]{4})([0-9]{0,2})$', views.order_count, name='order_count'),
    # url(r'^chansales/([0-9]{4})([0-9]{0,2})$', views.channal_salesamount_month, name='channal_salesamount_month'),


    # url(r'sendsms/(?P<cellphone>\d{11})$', demo_sms_send.send_sms, name='sendsms'),
]