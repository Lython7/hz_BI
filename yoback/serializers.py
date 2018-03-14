from rest_framework import serializers
from . import models

# class LoginSerializer(serializers.Serializer):
#     uname = serializers.CharField()
#     upassword = serializers.CharField()

class GoodsClassifySerializer(serializers.ModelSerializer):
    '''
        商品分类表序列化
    '''
    # created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = models.GoodsClassify
        fields = (
            'catNo',
            'catName',

            'edited_by',
            # 'created_time',
            # 'modified_time',
            'is_delete',
        )




class GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GoodsList
        fields = (
            'id',
            'channel',
            'catNo',
            'skuNo',
            'skuName',
            'price',

            'edited_by',
            # 'created_time',
            # 'modified_time',
            'is_delete',
        )



class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SaleOrder
        fields = (
            'id',
            'channel',
            'orderdate',
            'ordertime',
            'orderNo',
            'customer',
            'cuscellphone',

            'province',
            'city',

            'skuNo',

            'amount',
            'price',
            'Sumprice',
            'discountprice',
            'orderPay',
            'promotion',

            'edited_by',
            # 'created_time',
            # 'modified_time',
            'is_delete',
        )



class RevokeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RevokeOrder
        fields = (
            'id',
            'channel',
            'rorderdate',
            'rordertime',
            'rorderNo',
            'orderNo',
            'skuNo',
            # skuName = models.CharField(max_length=50, null=False, verbose_name='sku名称')
            'ramount',
            'price',
            'discountprice',
            'revokeprice',
            'rorderPay',

            'edited_by',
            # 'created_time',
            # 'modified_time',
            'is_delete',
        )




