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


class Online_GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Online_GoodsList
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



class Online_SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Online_SaleOrder
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


class Online_RevokeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Online_RevokeOrder
        fields = (
            'id',
            'channel',
            'rorderdate',
            'rordertime',
            'rorderNo',
            'orderNo',
            'skuNo',
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

class TV_GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TV_GoodsList
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



class TV_SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TV_SaleOrder
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



class TV_RevokeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TV_RevokeOrder
        fields = (
            'id',
            'channel',
            'rorderdate',
            'rordertime',
            'rorderNo',
            'orderNo',
            'skuNo',
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



