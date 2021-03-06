# Generated by Django 2.0.2 on 2018-04-19 14:47

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
            name='AdjustPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjustdate', models.DateField(verbose_name='调价日期')),
                ('adjusttime', models.TimeField(verbose_name='调价时间')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('skuName', models.CharField(max_length=50, verbose_name='sku名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsClassify',
            fields=[
                ('catNo', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='分类编码')),
                ('catName', models.CharField(max_length=20, verbose_name='分类名称')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='Online_GoodsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('skuName', models.CharField(max_length=50, verbose_name='sku名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('catNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoback.GoodsClassify', verbose_name='分类编码')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '商品清单',
                'verbose_name_plural': '商品清单',
            },
        ),
        migrations.CreateModel(
            name='Online_RevokeOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('rorderdate', models.DateField(verbose_name='订单日期')),
                ('rordertime', models.TimeField(verbose_name='下单时间')),
                ('rorderNo', models.CharField(max_length=30, verbose_name='退货订单号')),
                ('orderNo', models.CharField(max_length=20, verbose_name='订单编号')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('ramount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='退货数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('discountprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='折扣金额')),
                ('revokeprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='退货商品金额')),
                ('rorderPay', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='订单实付金额')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '退货订单',
                'verbose_name_plural': '退货订单',
            },
        ),
        migrations.CreateModel(
            name='Online_SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('orderdate', models.DateField(verbose_name='订单日期')),
                ('ordertime', models.TimeField(verbose_name='下单时间')),
                ('orderNo', models.CharField(max_length=20, verbose_name='订单编号')),
                ('customer', models.CharField(max_length=20, verbose_name='客户姓名')),
                ('cuscellphone', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='联系电话')),
                ('province', models.CharField(max_length=30, verbose_name='省')),
                ('city', models.CharField(max_length=30, verbose_name='市')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('Sumprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品总金额')),
                ('discountprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='折扣金额')),
                ('orderPay', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='订单实付金额')),
                ('promotion', models.CharField(max_length=50, verbose_name='优惠活动')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '销售订单',
                'verbose_name_plural': '销售订单',
            },
        ),
        migrations.CreateModel(
            name='TV_GoodsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('skuName', models.CharField(max_length=50, verbose_name='sku名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('catNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoback.GoodsClassify', verbose_name='分类编码')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '商品清单',
                'verbose_name_plural': '商品清单',
            },
        ),
        migrations.CreateModel(
            name='TV_RevokeOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('rorderdate', models.DateField(verbose_name='订单日期')),
                ('rordertime', models.TimeField(verbose_name='下单时间')),
                ('rorderNo', models.CharField(max_length=30, verbose_name='退货订单号')),
                ('orderNo', models.CharField(max_length=20, verbose_name='订单编号')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('ramount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='退货数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('discountprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='折扣金额')),
                ('revokeprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='退货商品金额')),
                ('rorderPay', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='订单实付金额')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '退货订单',
                'verbose_name_plural': '退货订单',
            },
        ),
        migrations.CreateModel(
            name='TV_SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=30, verbose_name='销售渠道')),
                ('orderdate', models.DateField(verbose_name='订单日期')),
                ('ordertime', models.TimeField(verbose_name='下单时间')),
                ('orderNo', models.CharField(max_length=20, verbose_name='订单编号')),
                ('customer', models.CharField(max_length=20, verbose_name='客户姓名')),
                ('cuscellphone', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='联系电话')),
                ('province', models.CharField(max_length=30, verbose_name='省')),
                ('city', models.CharField(max_length=30, verbose_name='市')),
                ('skuNo', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='sku编码')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品单价')),
                ('Sumprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品总金额')),
                ('discountprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='折扣金额')),
                ('orderPay', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='订单实付金额')),
                ('promotion', models.CharField(max_length=50, verbose_name='优惠活动')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('is_delete', models.BooleanField(choices=[(False, '保存'), (True, '删除')], default=False, verbose_name='逻辑删除')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人')),
            ],
            options={
                'verbose_name': '销售订单',
                'verbose_name_plural': '销售订单',
            },
        ),
    ]
