from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^incometoday/', views.today_income, name='income_today'), # 今日营收
    url(r'^salesamount/', views.sales_amount, name='sales_amount'), # 销售额
    url(r'^storecount/', views.store_count, name='store_count'), # 新增客户数
    url(r'^orderstorecount/', views.orderstore_count, name='orderstore_count'), # 下单客户数
    url(r'^ordercount/', views.order_count, name='order_count'), # 订单数量

    url(r'^channal_salesamount_month/', views.channal_salesamount_month, name='channal_salesamount_month'), # 本月各渠道销售额
    url(r'^salestrend/', views.sales_trend, name='sales_trend'), # 月销售趋势
    url(r'^classify_amount_month/', views.classify_amount_month, name='classify_amount_month'), # 月销售商品分类

    url(r'^region_amount_month/', views.region_amount_month, name='region_amount_month'), # 月区域销售额排名
    url(r'^score/(?P<year>.+)/(?P<month>.+)/', views.score, name='score'), # 销售人员额排名


    url(r'^ranking/', views.ranking, name='ranking'), # 业绩排名link
    url(r'^goodscount/', views.goodscount, name='goodscount'), # 商品统计link

    # url(r'sendsms/(?P<cellphone>\d{11})$', demo_sms_send.send_sms, name='sendsms'),

]