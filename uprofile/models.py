from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Uprofile(models.Model):
    '''
        如何定义必填项的话，需要先创建好admin用户后，将null改为False，重新迁移数据库，然后后台创建时候，该字段为必填项。
    '''
    choices_t = (
        (1, '前端登录 总经理'),
        (2, '前端登录 副总经理'),
        (3, '前端登录 大区经理'),
        (4, '前端登录 产品部经理'),
        (5, '前端登录 北京招商部经理'),
        (6, '前端登录 北京招商部主管'),
        (7, '前端登录 北京招商部专员'),
        (8, '前端登录 直营事业部经理'),
        (9, '前端登录 电视直销部经理'),
        (10, '前端登录 电子商务部经理'),
        (11, '前端登录 数据分析人员'),
        (12, '前端登录 其他人员'),

        (100, '后台登录 上帝权限'),# 上帝权限
        (101, '后台登录 后台管理'),# 无权
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
    uposition = models.IntegerField(choices=choices_t, default=12, verbose_name='用户角色', help_text='权限设定')
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
            # 此处需要根据权限 save配置权限表格

post_save.connect(create_user_profile, sender=User)


# class Permissions_F1(models.Model):
#     '''权限数据库，前端页面展示获取展示块内容'''
#
#     choices = (
#         (1, '有查看权限'),
#         (0, '无查看权限'),
#     )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
#
#     income_choices = (
#         (1, '全国数据'),
#         (2, '大区数据'),
#         (3, '电商数据'),
#         (4, '电视数据'),
#
#         (5, 'B2B全部数据'),
#
#         (11, 'B2B北京数据'),
#         (12, 'B2B华北数据'),
#         (13, 'B2B双鸭山数据'),
#         (14, 'B2B东北数据'),
#         (15, 'B2B华南数据'),
#         (16, 'B2B西南数据'),
#         (17, 'B2B北方数据'),
#         (18, 'B2B华东数据'),
#         (19, 'B2B西北数据'),
#         (20, 'B2B中原数据'),
#
#
#         (6, '直营店数据'),
#         (7, '禾中农业数据'),
#         (8, '禾中味道数据'),
#         (0, '无查看权限'),
#     )
#     today_income = models.IntegerField(choices=income_choices, default=0, verbose_name='今日营收')
#
#     sales_amount = models.IntegerField(choices=choices, default=0, verbose_name='销售额')
#     new_customer_count = models.IntegerField(choices=choices, default=0, verbose_name='新增客户数')
#     ordered_customer_count = models.IntegerField(choices=choices, default=0, verbose_name='下单客户数')
#     order_amount = models.IntegerField(choices=choices, default=0, verbose_name='订单数量')
#     channel_total = models.IntegerField(choices=choices, default=0, verbose_name='本月各渠道销售额')
#     sales_trend = models.IntegerField(choices=choices, default=0, verbose_name='道销趋势')
#     classify_sale_status = models.IntegerField(choices=choices, default=0, verbose_name='本月商品分类销售额')
#     regional_sales_amount = models.IntegerField(choices=choices, default=0, verbose_name='本月区域销售额')
#     B2Bsalesman_TOP3 = models.IntegerField(choices=choices, default=0, verbose_name='本月B2B销售人员TOP3')
#
#     class Meta:
#         verbose_name = '用户权限配置表'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.user)
#
#     def __unicode__(self):
#         return str(self.user)
#
# class Permissions_F2(object):
#     '''权限数据库，前端页面展示获取展示块内容'''
#
#     choices = (
#         (1, '有查看权限'),
#         (0, '无查看权限'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
#     #     upower = models.IntegerField(choices=choices_t, default=5, verbose_name='用户角色', help_text='权限设定')
#
#     channel_total = models.IntegerField(choices=choices, default=0, verbose_name='各渠道销售额')
#     sales_trend = models.IntegerField(choices=choices, default=0, verbose_name='道销趋势')
#     goofs_count = models.IntegerField(choices=choices, default=0, verbose_name='商品统计')
#     regional_count = models.IntegerField(choices=choices, default=0, verbose_name='区域统计')
#
#
#     class Meta:
#         verbose_name = '用户权限配置表-探索'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.user
#
#     def __unicode__(self):
#         return self.user
