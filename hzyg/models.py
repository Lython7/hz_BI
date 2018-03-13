from django.db import models

# Create your models here.
class b2b_goodstable(models.Model):
    createDate = models.DateField(null=False, verbose_name='创建日期')
    organName = models.CharField(max_length=64, verbose_name='机构名称')
    orderStoreName = models.CharField(max_length=64, verbose_name='订单归属门店名称')
    orderNo = models.CharField(max_length=32, verbose_name='单据编号', null=False)
    tbNo = models.CharField(max_length=32)
    secondIcatName = models.CharField(max_length=64)
    skuCode = models.CharField(max_length=16)
    skuName = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='数量')
    memberPin = models.CharField(max_length=64, verbose_name='会员用户名')
    regionName = models.CharField(max_length=254, default='', verbose_name='地区名称')
    realName = models.CharField(max_length=32, verbose_name='用户姓名')
    supName = models.CharField(max_length=64)

    class Meta:
        db_table = 'b2b_goodstable'



class b2b_ordertable(models.Model):
    createDate = models.DateField(null=False, verbose_name='创建日期')
    organName = models.CharField(max_length=64, verbose_name='机构名称')
    orderStoreName = models.CharField(max_length=64, verbose_name='订单归属门店名称')
    orderNo1 = models.CharField(max_length=32, verbose_name='单据编号1')
    orderNo2 = models.CharField(max_length=32, verbose_name='单据编号2')
    orderNo3 = models.CharField(max_length=32, verbose_name='单据编号3')
    realPayAmount = models.DecimalField(max_digits=16, decimal_places=5, verbose_name='客户实际支付的金额')
    amount = models.DecimalField(max_digits=22, decimal_places=5, verbose_name='数量')
    memberPin = models.CharField(max_length=64, verbose_name='会员用户名')
    regionName = models.CharField(max_length=254, default='', verbose_name='地区名称')
    realName = models.CharField(max_length=32, verbose_name='用户姓名')

    class Meta:
        db_table = 'b2b_ordertable'