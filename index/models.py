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

    catNo = models.IntegerField(null=False, primary_key=True, verbose_name='分类编码')
    catName = models.CharField(max_length=20, null=False, verbose_name='分类名称')

    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False)  # 编辑人 editable=False default =当前登录的id
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.catname


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

    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False)  # 编辑人 editable=False default =当前登录的id
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '商品清单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.skuName + self.channel