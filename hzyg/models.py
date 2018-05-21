from django.db import models

# Create your models here.
class b2b_goodstable(models.Model):
    createDate = models.DateTimeField(verbose_name='创建日期')
    organName = models.CharField(max_length=64, verbose_name='机构名称')
    orderStore = models.CharField(max_length=16, verbose_name='订单店铺')
    orderStoreName = models.CharField(max_length=64, verbose_name='订单归属门店名称')
    orderNo = models.CharField(max_length=32, verbose_name='单据编号')
    tbNo = models.CharField(max_length=32)
    secondIcatName = models.CharField(max_length=64)
    # secondIcatName = models.CharField(max_length=64)
    skuCode = models.CharField(max_length=16)
    skuName = models.CharField(max_length=100)
    skuNum = models.DecimalField(max_digits=16, decimal_places=5, verbose_name='skuNum')
    realSkuNum = models.DecimalField(max_digits=22, decimal_places=5, verbose_name='realSkuNum')
    amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='数量')
    memberPin = models.CharField(max_length=64, verbose_name='会员用户名')
    regionName = models.CharField(max_length=254, default='', verbose_name='地区名称')
    realName = models.CharField(max_length=32, verbose_name='用户姓名')
    supName = models.CharField(max_length=64)
    orderStatus = models.IntegerField(null=True)
    payMode = models.IntegerField(null=True)

    class Meta:
        db_table = 'b2b_goodstable'



class b2b_ordertable(models.Model):
    createDate = models.DateTimeField(verbose_name='创建日期')
    organName = models.CharField(max_length=64, verbose_name='机构名称')
    orderStore = models.CharField(max_length=16, verbose_name='订单店铺')
    orderStoreName = models.CharField(max_length=64, verbose_name='订单归属门店名称')
    orderNo = models.CharField(max_length=32, verbose_name='单据编号')
    tbNo1 = models.CharField(max_length=32, verbose_name='tbNo1')
    tbNo2 = models.CharField(max_length=32, verbose_name='tbNo2')
    # orderNo2 = models.CharField(max_length=32, verbose_name='单据编号2')
    # orderNo3 = models.CharField(max_length=32, verbose_name='单据编号3')
    realPayAmount = models.DecimalField(max_digits=16, decimal_places=5, verbose_name='客户实际支付的金额')
    coupon = models.DecimalField(max_digits=26, decimal_places=9)
    amount = models.DecimalField(max_digits=22, decimal_places=5, verbose_name='数量')
    memberPin = models.CharField(max_length=64, verbose_name='会员用户名')
    regionName = models.CharField(max_length=254, default='', verbose_name='地区名称')
    realName = models.CharField(max_length=32, verbose_name='用户姓名')
    orderStatus = models.IntegerField(null=True)
    payMode = models.IntegerField(null=True)

    # id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'b2b_ordertable'


class b2b_posgoods(models.Model):
    createDate = models.DateTimeField(verbose_name='创建日期')
    orderStore = models.IntegerField(verbose_name='订单店铺')
    orderStoreName = models.CharField(max_length=40, verbose_name='订单归属门店名称')
    organCode = models.IntegerField()
    organName = models.CharField(max_length=40)
    orderNo = models.CharField(max_length=40)
    secondIcatName = models.CharField(max_length=40)
    skuCode = models.CharField(max_length=40)
    skuName = models.CharField(max_length=40)
    skuNum = models.DecimalField(max_digits=22, decimal_places=5)
    amount = models.DecimalField(max_digits=22, decimal_places=5, verbose_name='数量')
    realPayAmount = models.DecimalField(max_digits=22, decimal_places=5)

    class Meta:
        db_table = 'b2b_posgoods'


class b2b_storeb2b(models.Model):
    # id = models.AutoField(primary_key=True)
    ownerno = models.CharField(max_length=32)
    ownerPin = models.CharField(max_length=64)
    ownerName = models.CharField(max_length=32)
    cellphone = models.CharField(max_length=16)
    shopName = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    status = models.IntegerField()
    areaCode = models.CharField(max_length=32)
    areaName = models.CharField(max_length=64)
    levelCode = models.CharField(max_length=32)
    levelName = models.CharField(max_length=64)
    recomm_username = models.CharField(max_length=64)
    sales_username = models.CharField(max_length=32)
    sales_cell = models.CharField(max_length=16)
    created_dt = models.DateTimeField()

    class Meta:
        db_table = 'b2b_storeb2b'