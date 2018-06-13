from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Show_overview(models.Model):
    '''前端页面展示获取展示块内容-今日营收'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)

    income_choices = (
        (0, '无查看权限'),
        (1, '全国数据'),
        (2, '电商数据'),
        (3, '电视数据'),

        (4, 'B2B全部数据'),

        (5, 'B2B北京数据'),
        (6, 'B2B华北数据'),
        (7, 'B2B双鸭山数据'),
        (8, 'B2B东北数据'),
        (9, 'B2B华南数据'),
        (10, 'B2B西南数据'),
        (11, 'B2B北方数据'),
        (12, 'B2B华东数据'),
        (13, 'B2B西北数据'),
        (14, 'B2B中原数据'),

        (15, '直营店数据'),
        (16, '禾中农业数据'),
        (17, '禾中味道数据'),

    )
    today_income = models.IntegerField(choices=income_choices, default=0, verbose_name='今日营收')
    sales_amount = models.IntegerField(choices=income_choices, default=0, verbose_name='销售额')
    store_count = models.IntegerField(choices=income_choices, default=0, verbose_name='新增客户数')
    orderstore_count = models.IntegerField(choices=income_choices, default=0, verbose_name='下单客户数')
    order_count = models.IntegerField(choices=income_choices, default=0, verbose_name='订单数量')
    channal_salesamount_month = models.IntegerField(choices=income_choices, default=0, verbose_name='本月各渠道销售额')
    sales_trend = models.IntegerField(choices=income_choices, default=0, verbose_name='销售趋势')
    classify_amount_month = models.IntegerField(choices=income_choices, default=0, verbose_name='本月商品分类销售额')
    area_salesamount_month = models.IntegerField(choices=income_choices, default=0, verbose_name='本月区域销售额')
    B2B_TOP3_month = models.IntegerField(choices=income_choices, default=0, verbose_name='本月B2B销售人员TOP3')

    class Meta:
        verbose_name = '今日营收显示选择'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)