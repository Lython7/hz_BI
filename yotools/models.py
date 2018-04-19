from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class SMSCode(models.Model):
    choices = ((1, '有效'),(2, '失效'),)
    phone_number = models.CharField(max_length=11)
    code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now=True)
    stutas = models.IntegerField(choices=choices)
    timeflag = models.CharField(max_length=100)
