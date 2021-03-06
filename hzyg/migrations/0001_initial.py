# Generated by Django 2.0.2 on 2018-04-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='b2b_goodstable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateField(verbose_name='创建日期')),
                ('organName', models.CharField(max_length=64, verbose_name='机构名称')),
                ('orderStoreName', models.CharField(max_length=64, verbose_name='订单归属门店名称')),
                ('orderNo', models.CharField(max_length=32, verbose_name='单据编号')),
                ('tbNo', models.CharField(max_length=32)),
                ('secondIcatName', models.CharField(max_length=64)),
                ('skuCode', models.CharField(max_length=16)),
                ('skuName', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='数量')),
                ('memberPin', models.CharField(max_length=64, verbose_name='会员用户名')),
                ('regionName', models.CharField(default='', max_length=254, verbose_name='地区名称')),
                ('realName', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('supName', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'b2b_goodstable',
            },
        ),
        migrations.CreateModel(
            name='b2b_ordertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateField(verbose_name='创建日期')),
                ('organName', models.CharField(max_length=64, verbose_name='机构名称')),
                ('orderStoreName', models.CharField(max_length=64, verbose_name='订单归属门店名称')),
                ('orderNo1', models.CharField(max_length=32, verbose_name='单据编号1')),
                ('orderNo2', models.CharField(max_length=32, verbose_name='单据编号2')),
                ('orderNo3', models.CharField(max_length=32, verbose_name='单据编号3')),
                ('realPayAmount', models.DecimalField(decimal_places=5, max_digits=16, verbose_name='客户实际支付的金额')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=22, verbose_name='数量')),
                ('memberPin', models.CharField(max_length=64, verbose_name='会员用户名')),
                ('regionName', models.CharField(default='', max_length=254, verbose_name='地区名称')),
                ('realName', models.CharField(max_length=32, verbose_name='用户姓名')),
            ],
            options={
                'db_table': 'b2b_ordertable',
            },
        ),
    ]
