from django.db import models

# Create your models here.
class GoodsClassify(models.Model):
    '''
        商品分类 所有渠道通用的 写死的 不需要变动的
    '''
    choices = (
        (False, '保存'),
        (True, '删除'),
    )
    catNo = models.CharField(max_length=20, null=False, verbose_name='分类编码')
    catName = models.CharField(max_length=20, null=False, verbose_name='分类名称')

    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False, on_delete=models.CASCADE)  # 编辑人 editable=False default =当前登录的id
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间', null=False)
    modified_time = models.DateTimeField(auto_now=True, editable=False, verbose_name='编辑时间', null=False)
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.catName


class GoodsList(models.Model):
    '''
        商品清单 各自维护各自的清单？？？？？？
    '''
    choices = (
        (False, '保存'),
        (True, '删除'),
    )

    channel = models.CharField(max_length=30, null=False, verbose_name='销售渠道')
    classifyNo = models.ForeignKey(GoodsClassify, on_delete=models.CASCADE, null=False, verbose_name='分类编码')
    skuNo = models.CharField(max_length=10, null=False, verbose_name='sku编码')
    skuName = models.CharField(max_length=50, null=False, verbose_name='sku名称')
    price = models.CharField(max_length=5, null=False, verbose_name='商品单价')

    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False, on_delete=models.CASCADE)  # 编辑人 editable=False default =当前登录的id
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间', null=False)
    modified_time = models.DateTimeField(auto_now=True, editable=False, verbose_name='编辑时间', null=False)
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '商品清单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.skuName + self.channel


class SaleOrder(models.Model):
    '''销售订单'''
    choices = (
        (False, '保存'),
        (True, '删除'),
    )

    channel = models.CharField(max_length=30, null=False, verbose_name='销售渠道')
    orderdate = models.DateField(verbose_name='订单日期', null=False)
    ordertime = models.TimeField(verbose_name='下单时间', null=False)
    orderNo = models.CharField(max_length=30, null=False, verbose_name='订单编号')
    customer = models.CharField(max_length=20, null=False, verbose_name='客户姓名')
    cuscellphone = models.CharField(max_length=11, null=False, verbose_name='联系电话')

    province = models.CharField(max_length=30, null=False, verbose_name='省')
    city = models.CharField(max_length=30, null=False, verbose_name='市')
    area = models.CharField(max_length=30, null=False, verbose_name='区')

    skuNo = models.CharField(max_length=10, null=False, verbose_name='sku编码')
    skuName = models.CharField(max_length=50, null=False, verbose_name='sku名称')
    amount = models.CharField(max_length=6, null=False, verbose_name='数量')
    price = models.CharField(max_length=6, null=False, verbose_name='商品单价')
    Sumprice = models.CharField(max_length=6, null=False, verbose_name='商品总金额')
    discountprice = models.CharField(max_length=6, null=False, verbose_name='折扣金额')
    orderPay= models.CharField(max_length=6, null=False, verbose_name='订单实付金额')
    promotion= models.CharField(max_length=20, null=False, verbose_name='优惠活动')

    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False, on_delete=models.CASCADE)  # 编辑人 editable=False default =当前登录的id
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间', null=False)
    modified_time = models.DateTimeField(auto_now=True, editable=False, verbose_name='编辑时间', null=False)
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '销售订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.orderNo


class RevokeOrder(models.Model):
    '''退货订单'''
    choices = (
        (False, '保存'),
        (True, '删除'),
    )

    channel = models.CharField(max_length=30, null=False, verbose_name='销售渠道')
    rorderdate = models.DateField(verbose_name='订单日期', null=False)
    rordertime = models.TimeField(verbose_name='下单时间', null=False)
    rorderNo = models.CharField(max_length=30, null=False, verbose_name='退货订单号')
    orderNo = models.CharField(max_length=30, null=False, verbose_name='订单编号')
    skuNo = models.CharField(max_length=10, null=False, verbose_name='sku编码')
    skuName = models.CharField(max_length=50, null=False, verbose_name='sku名称')
    ramount = models.CharField(max_length=6, null=False, verbose_name='退货数量')
    price = models.CharField(max_length=6, null=False, verbose_name='商品单价')
    discountprice = models.CharField(max_length=6, null=False, verbose_name='折扣金额')
    revokeprice= models.CharField(max_length=6, null=False, verbose_name='退货商品金额')
    orderPay= models.CharField(max_length=6, null=False, verbose_name='订单实付金额')

    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False, on_delete=models.CASCADE)  # 编辑人 editable=False default =当前登录的id
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间', null=False)
    modified_time = models.DateTimeField(auto_now=True, editable=False, verbose_name='编辑时间', null=False)
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '退货订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.rorderNo