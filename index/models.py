from django.db import models

# Create your models here.
class GoodsClassify(models.Model):
    '''
        商品分类 所有渠道通用的 写死的 不需要变动的
    '''
    catNo = models.IntegerField(null=False, primary_key=True)
    catname = models.CharField(max_length=20, null=False)

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.catname


class GoodsList(models.Model):
    '''
        商品清单 各自维护各自的清单？？？？？？
    '''
    channel = models.CharField(max_length=30, null=False)
    classifyNo = models.ForeignKey(GoodsClassify, on_delete=models.CASCADE, null=False)
    skuNo = models.CharField(max_length=10, null=False)
    skuName = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=5, null=False)

    class Meta:
        verbose_name = '商品清单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.skuName + self.channel