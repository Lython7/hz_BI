# Generated by Django 2.0.2 on 2018-04-19 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=32, null=True, verbose_name='用户姓名')),
                ('ucellphone', models.CharField(max_length=11, unique=True, verbose_name='手机号码')),
                ('upower', models.IntegerField(choices=[(1, '前端登录 总经理 查看权限'), (2, '前端登录 大区经理 查看权限'), (3, '前端登录 部门经理 查看权限'), (4, '前端登录 招商人员 查看权限'), (5, '前端登录 数据分析人员 查看权限'), (6, '前端登录 其他人员 查看权限'), (100, '后台登录 上帝权限'), (101, '后台登录 禾中优供 数据维护权限'), (102, '后台登录 电商平台 数据维护权限'), (103, '后台登录 电视购物 数据维护权限'), (104, '后台登录 后台管理')], default=5, help_text='权限设定', verbose_name='用户角色')),
                ('ustatus', models.IntegerField(choices=[(1, '已审核'), (0, '待审核'), (-1, '审核未通过'), (-2, '已删除')], default=0, verbose_name='用户状态')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户信息拓展表',
                'verbose_name_plural': '用户信息拓展表',
            },
        ),
    ]
