from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Uprofile(models.Model):
    '''
        如何定义必填项的话，需要先创建好admin用户后，将null改为False，重新迁移数据库，然后后台创建时候，该字段为必填项。
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    uname = models.CharField(max_length=32, null=True, verbose_name='用户姓名')
    ucellphone = models.CharField(max_length=11, null=True, verbose_name='手机号码', unique=True)
    uposition = models.CharField(max_length=32, null=True, verbose_name='工作岗位')

    class Meta:
        verbose_name = '用户信息拓展表'
        verbose_name_plural = verbose_name

    # 重写save方法，最后判断完成后，调用父类save方法。
    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                profile = Uprofile.objects.get(user=self.user)
                self.pk = profile.pk
            except Uprofile.DoesNotExist:
                pass
        super(Uprofile, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Uprofile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)