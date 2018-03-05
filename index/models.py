from django.db import models

# Create your models here.
class GoodsClassify(models.Model):
    '''
        商品分类 写死的 不需要变动的
    '''
    catNo = models.IntegerField(null=False)
    catname = models.CharField(max_length=20, null=False)

    class Meta:
        # db_table = ''
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.catname



