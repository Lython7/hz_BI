from django.db import models

# Create your models here.
class sale_upload(models.Model):
    choices = ((1,'已审核'),
               (0,'待审核'),
               (-1,'无效数据'),
               )
    createdate = models.DateField()
    salesname = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)
    imageurl = models.CharField(max_length=256)
    checkif = models.IntegerField(default=0)
    class Meta:
        db_table = 'sale_upload'