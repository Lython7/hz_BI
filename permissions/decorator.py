from django.forms import model_to_dict
from django.http import JsonResponse

from overview.models import Show_overview
from .models import *
# 权限装饰器

# 1、今日营收 看看这个人今日营收应该看哪部分

def tdincome_which(func):
    '''今日营收'''
    def inner(request):
    # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
            }
        try:
            datashow = choices[Show_overview.objects.get(user=request.user).today_income]
            queryset = Permissions_P1.objects.get(user=request.user)
            datadic = model_to_dict(queryset)
        except:
            return JsonResponse({'res': '没有权限'})
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def sales_amount_which(func):
    '''销售额'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).sales_amount]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner


def store_count_which(func):
    '''新增客户数'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).store_count]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def orderstore_count_which(func):
    '''下单客户数'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).orderstore_count]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def order_count_which(func):
    '''订单数量'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).order_count]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def channal_salesamount_month_which(func):
    '''本月各渠道销售额'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).channal_salesamount_month]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def sales_trend_which(func):
    '''销售趋势-本月'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).sales_trend]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def classify_amount_month_which(func):
    '''本月商品分类销售额'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).classify_amount_month]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def area_salesamount_month_which(func):
    '''本月区域销售额'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).area_salesamount_month]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner

def B2B_TOP3_month_which(func):
    '''本月B2B销售人员TOP3'''
    def inner(request):
        # 如果modles记录是哪个区域 就查看相应区域是否有权限
        choices = {
            0: 'no_permissions',
            1: 'whole_country',
            2: 'business_online',
            3: 'television_shopping',

            4: 'B2B_all',

            5: 'B2B_beijing',
            6: 'B2B_huabei',
            7: 'B2B_shuangyashan',
            8: 'B2B_dongbei',
            9: 'B2B_huanan',
            10: 'B2B_xinan',
            11: 'B2B_beifang',
            12: 'B2B_huadong',
            13: 'B2B_xibei',
            14: 'B2B_zhongyuan',

            15: 'direct_store',
            16: 'hz_agricultural',
            17: 'hz_taste',
        }

        datashow = choices[Show_overview.objects.get(user=request.user).B2B_TOP3_month]
        queryset = Permissions_P2.objects.get(user=request.user)
        datadic = model_to_dict(queryset)
        # print(datadic)
        if datadic[datashow] == 1:
            ret = func(request)
            return ret
        else:
            return JsonResponse({'res': '没有权限'})
    return inner