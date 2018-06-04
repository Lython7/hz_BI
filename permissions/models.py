from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Permissions_P1(models.Model):
    '''今日营收'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_今日营收'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P2(models.Model):
    '''销售额'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_销售额'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P3(models.Model):
    '''新增客户数'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_新增客户数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P4(models.Model):
    '''下单客户数'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_下单客户数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P5(models.Model):
    '''订单数量'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_订单数量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P6(models.Model):
    '''本月渠道销售额'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_本月渠道销售额'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P7(models.Model):
    '''销售趋势'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_销售趋势'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P8(models.Model):
    '''本月商品分类销售额'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_本月商品分类销售额'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)

class Permissions_P9(models.Model):
    '''本月区域销售额'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_本月区域销售额'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)


class Permissions_P10(models.Model):
    '''本月B2B销售人员TOP3'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', primary_key=True)
    choices = (
        (1, '有查看权限'),
        (0, '无权限'),
    )
    overall = models.IntegerField(choices=choices, default=0, verbose_name='总权限')

    whole_country = models.IntegerField(choices=choices, default=0, verbose_name='全国数据')
    business_online = models.IntegerField(choices=choices, default=0, verbose_name='电子商务数据')
    television_shopping = models.IntegerField(choices=choices, default=0, verbose_name='电视购物数据')

    B2B_all = models.IntegerField(choices=choices, default=0, verbose_name='B2B全部数据')

    B2B_beijing = models.IntegerField(choices=choices, default=0, verbose_name='B2B北京数据')
    B2B_huabei = models.IntegerField(choices=choices, default=0, verbose_name='B2B华北数据')
    B2B_shuangyashan = models.IntegerField(choices=choices, default=0, verbose_name='B2B双鸭山数据')
    B2B_dongbei = models.IntegerField(choices=choices, default=0, verbose_name='B2B东北数据')
    B2B_huanan = models.IntegerField(choices=choices, default=0, verbose_name='B2B华南数据')
    B2B_xinan = models.IntegerField(choices=choices, default=0, verbose_name='B2B西南数据')
    B2B_beifang = models.IntegerField(choices=choices, default=0, verbose_name='B2B北方数据')
    B2B_huadong = models.IntegerField(choices=choices, default=0, verbose_name='B2B华东数据')
    B2B_xibei = models.IntegerField(choices=choices, default=0, verbose_name='B2B西北数据')
    B2B_zhongyuan = models.IntegerField(choices=choices, default=0, verbose_name='B2B中原数据')

    direct_store = models.IntegerField(choices=choices, default=0, verbose_name='直营店数据')
    hz_agricultural = models.IntegerField(choices=choices, default=0, verbose_name='禾中农业数据')
    hz_taste = models.IntegerField(choices=choices, default=0, verbose_name='禾中味道数据')

    class Meta:
        verbose_name = '权限配置_本月B2B销售人员TOP3'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)





