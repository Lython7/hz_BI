# Generated by Django 2.0.2 on 2018-05-29 11:20

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
            name='Show_overview',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('today_income', models.IntegerField(choices=[(0, '无查看权限'), (1, '全国数据'), (2, '电商数据'), (3, '电视数据'), (4, 'B2B全部数据'), (5, 'B2B北京数据'), (6, 'B2B华北数据'), (7, 'B2B双鸭山数据'), (8, 'B2B东北数据'), (9, 'B2B华南数据'), (10, 'B2B西南数据'), (11, 'B2B北方数据'), (12, 'B2B华东数据'), (13, 'B2B西北数据'), (14, 'B2B中原数据'), (15, '直营店数据'), (16, '禾中农业数据'), (17, '禾中味道数据')], default=0, verbose_name='今日营收')),
                ('sales_amount', models.IntegerField(choices=[(0, '无查看权限'), (1, '全国数据'), (2, '电商数据'), (3, '电视数据'), (4, 'B2B全部数据'), (5, 'B2B北京数据'), (6, 'B2B华北数据'), (7, 'B2B双鸭山数据'), (8, 'B2B东北数据'), (9, 'B2B华南数据'), (10, 'B2B西南数据'), (11, 'B2B北方数据'), (12, 'B2B华东数据'), (13, 'B2B西北数据'), (14, 'B2B中原数据'), (15, '直营店数据'), (16, '禾中农业数据'), (17, '禾中味道数据')], default=0, verbose_name='销售额')),
            ],
            options={
                'verbose_name': '今日营收显示选择',
                'verbose_name_plural': '今日营收显示选择',
            },
        ),
    ]