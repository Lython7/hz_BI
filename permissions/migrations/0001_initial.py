# Generated by Django 2.0.2 on 2018-05-28 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions_P1',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('overall', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='总权限')),
                ('whole_country', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='全国数据')),
                ('business_online', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='电子商务数据')),
                ('television_shopping', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='电视购物数据')),
                ('B2B_all', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B全部数据')),
                ('B2B_beijing', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B北京数据')),
                ('B2B_huabei', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B华北数据')),
                ('B2B_shuangyashan', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B双鸭山数据')),
                ('B2B_dongbei', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B东北数据')),
                ('B2B_huanan', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B华南数据')),
                ('B2B_xinan', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B西南数据')),
                ('B2B_beifang', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B北方数据')),
                ('B2B_huadong', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B华东数据')),
                ('B2B_xibei', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B西北数据')),
                ('B2B_zhongyuan', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='B2B中原数据')),
                ('direct_store', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='直营店数据')),
                ('hz_agricultural', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='禾中农业数据')),
                ('hz_taste', models.IntegerField(choices=[(1, '有查看权限'), (0, '无查看权限')], default=0, verbose_name='禾中味道数据')),
            ],
            options={
                'verbose_name': '权限配置',
                'verbose_name_plural': '权限配置',
            },
        ),
        migrations.CreateModel(
            name='Permissions_tdincome',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('today_income', models.IntegerField(choices=[(0, '无查看权限'), (1, '全国数据'), (2, '电商数据'), (3, '电视数据'), (4, 'B2B全部数据'), (5, 'B2B北京数据'), (6, 'B2B华北数据'), (7, 'B2B双鸭山数据'), (8, 'B2B东北数据'), (9, 'B2B华南数据'), (10, 'B2B西南数据'), (11, 'B2B北方数据'), (12, 'B2B华东数据'), (13, 'B2B西北数据'), (14, 'B2B中原数据'), (15, '直营店数据'), (16, '禾中农业数据'), (17, '禾中味道数据')], default=0, verbose_name='今日营收')),
            ],
            options={
                'verbose_name': '今日营收显示选择',
                'verbose_name_plural': '今日营收显示选择',
            },
        ),
    ]
