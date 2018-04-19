from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Uprofile(models.Model):
    '''
        如何定义必填项的话，需要先创建好admin用户后，将null改为False，重新迁移数据库，然后后台创建时候，该字段为必填项。
    '''

    choices = (
        (1, '前端登录 总经理 查看权限'),
        (2, '前端登录 大区经理 查看权限'),
        (3, '前端登录 部门经理 查看权限'),
        (4, '前端登录 招商人员 查看权限'),
        (5, '前端登录 数据分析人员 查看权限'),
        (6, '前端登录 其他人员 查看权限'),

        (100, '后台登录 上帝权限'),# 上帝权限
        (101, '后台登录 禾中优供 数据维护权限'),# 禾中优供
        (102, '后台登录 电商平台 数据维护权限'),# 电商
        (103, '后台登录 电视购物 数据维护权限'),# 电视
        (104, '后台登录 后台管理'),# 无权
    )

    check_choices = (
        (1, '已审核'),
        (0, '待审核'),
        (-1, '审核未通过'),
        (-2, '已删除'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    uname = models.CharField(max_length=32, null=True, verbose_name='用户姓名')
    ucellphone = models.CharField(max_length=11, null=False, verbose_name='手机号码', unique=True)
    # uemail = models.CharField(max_length=32, null=False, unique=True, verbose_name='企业邮箱')
    # udepartment = models.CharField(max_length=32, null=True, verbose_name='部门', help_text='')
    # uposition = models.CharField(max_length=64, null=True, verbose_name='工作岗位')

    upower = models.IntegerField(choices=choices, default=5, verbose_name='用户角色', help_text='权限设定')
    ustatus = models.IntegerField(choices=check_choices, default=0, verbose_name='用户状态')


    class Meta:
        verbose_name = '用户信息拓展表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname

    def __unicode__(self):
        return self.uname

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

        if profile.user_id == 1:
            profile.uname = 'admin'
            profile.ucellphone = '18999999999'
            profile.upower = 100
            profile.ustatus = 1
            profile.save()
        else:
            profile.save()

post_save.connect(create_user_profile, sender=User)