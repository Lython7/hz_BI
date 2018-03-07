from rest_framework import serializers
from . import models

# class LoginSerializer(serializers.Serializer):
#     uname = serializers.CharField()
#     upassword = serializers.CharField()

# class GoodsClassifySerializer(serializers.ModelSerializer):
#     '''
#         商品分类表序列化
#     '''
#     # created_by = serializers.ReadOnlyField(source='created_by.username')
#
#     class Meta:
#         model = models.GoodsClassify
#         fields = (
#             'catNo',
#             'catName',
#             'created_time',
#             'created_by',
#             'is_delete',
#         )