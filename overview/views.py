import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.http import HttpResponse, JsonResponse

from hzyg.models import *
from uprofile.models import *


class incomeDay(object):
    '''营收数据'''

    def _get_permission(self, request):
        # 获取今日营收权限
        return request.session.get('permissions')['today_income']

    def _get_datetime(self, request):
        # 获取日期时间
        # _timenow = time.strftime("%Y-%m-%d-%H", time.localtime()).split('-')
        datetime = []
        datetime.append(request.GET.get('year', None))
        datetime.append(request.GET.get('month', None))
        datetime.append(request.GET.get('day', None))
        datetime.append(request.GET.get('hour', None))
        return datetime

    def _get_today(self):
        return time.strftime("%Y-%m-%d-%H", time.localtime()).split('-')

    def _get_queryset_list(self, request, year, month, day, _per=0):
        # 获取queryset
        querysetlist = []
        queryset1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)
        queryset2 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)
        queryset3 = b2b_store.objects.using('hzyg').filter(status=0, createDate__year=year, createDate__month=month, createDate__day=day)

        if _per == 0:
            pass
        elif _per == 1:
            querysetlist.append(queryset1)
            querysetlist.append(queryset2)
            querysetlist.append(queryset3)

        elif _per == 2:
            # 大区机构权限 分大区
            pass
            # querysetlist.append(queryset1)
            # querysetlist.append(queryset2)
            # querysetlist.append(queryset3)

        elif _per == 3:
            # 电商数据 京东官方直营店1013 民生银行仓库101014 九河泉101106
            querysetlist.append(queryset1.filter(Q(orderStore='1013') | Q(orderStore='101014') | Q(orderStore='101106')))
            querysetlist.append(queryset2.filter(Q(orderStore=1013) | Q(orderStore=101014) | Q(orderStore=101106)))
            querysetlist.append(queryset3.filter(Q(storeCode='1013') | Q(storeCode='101014') | Q(storeCode='101106')))

        elif _per == 4:
            # 电视购物数据 101103
            querysetlist.append(queryset1.filter(orderStore='101103'))
            querysetlist.append(queryset2.filter(orderStore=101103))
            querysetlist.append(queryset3.filter(storeCode='101103'))

        elif _per == 5:
            # B2B数据全部                               1010                  1011                         101101                 101102                  1012                      1016                 102101                    103101                   104101                    105101                  106101                   107101                   108101              109101               110101
            querysetlist.append(queryset1.filter(Q(orderStore='1010') | Q(orderStore='1011') | Q(orderStore='101101') | Q(orderStore='101102') | Q(orderStore='1012') | Q(orderStore='1016') | Q(orderStore='102101') | Q(orderStore='103101') | Q(orderStore='104101') | Q(orderStore='105101') | Q(orderStore='106101') | Q(orderStore='107101') | Q(orderStore='108101') | Q(orderStore='109101') | Q(orderStore='110101')))
            querysetlist.append(queryset2.filter(Q(orderStore=1010)   | Q(orderStore=1011)   | Q(orderStore=101101)   | Q(orderStore=101102)   | Q(orderStore=1012)   | Q(orderStore=1016)   | Q(orderStore=102101)   | Q(orderStore=103101)   | Q(orderStore=104101)   | Q(orderStore=105101)   | Q(orderStore=106101)   | Q(orderStore=107101)   | Q(orderStore=108101)   | Q(orderStore=109101)   | Q(orderStore=110101)))
            querysetlist.append(queryset3.filter(Q(storeCode='1010')  | Q(storeCode='1011')  | Q(storeCode='101101')  | Q(storeCode='101102')  | Q(storeCode='1012')  | Q(storeCode='1016')  | Q(storeCode='102101')  | Q(storeCode='103101')  | Q(storeCode='104101')  | Q(storeCode='105101')  | Q(storeCode='106101')  | Q(storeCode='107101')  | Q(storeCode='108101')  | Q(storeCode='109101')  | Q(storeCode='110101')))

        elif _per == 6:
            # 直营店1014
            querysetlist.append(queryset1.filter(orderStore='1014'))
            querysetlist.append(queryset2.filter(orderStore=1014))
            querysetlist.append(queryset3.filter(storeCode='1014'))


        elif _per == 7:
            # 禾中农业 禾中农业仓库 101105 农业订单 1015
            querysetlist.append(queryset1.filter(Q(orderStore='101105') | Q(orderStore='1015')))
            querysetlist.append(queryset2.filter(Q(orderStore=101105) | Q(orderStore=1015)))
            querysetlist.append(queryset3.filter(Q(storeCode='101105') | Q(storeCode='1015')))

        elif _per == 8:
            # 禾中味道  1201
            querysetlist.append(queryset1.filter(orderStore='1201'))
            querysetlist.append(queryset2.filter(orderStore=1201))
            querysetlist.append(queryset3.filter(storeCode='1201'))

        elif _per == 11:
            # B2B北京数据                             1010                  1011                         101101                 101102                  1012                      1016
            querysetlist.append(queryset1.filter(Q(orderStore='1010') | Q(orderStore='1011') | Q(orderStore='101101') | Q(orderStore='101102') | Q(orderStore='1012') | Q(orderStore='1016')))
            querysetlist.append(queryset2.filter(Q(orderStore=1010)   | Q(orderStore=1011)   | Q(orderStore=101101)   | Q(orderStore=101102)   | Q(orderStore=1012)   | Q(orderStore=1016)))
            querysetlist.append(queryset3.filter(Q(storeCode='1010')  | Q(storeCode='1011')  | Q(storeCode='101101')  | Q(storeCode='101102')  | Q(storeCode='1012')  | Q(storeCode='1016')))

        elif _per == 12:
            # b2b华北数据 102101
            querysetlist.append(queryset1.filter(Q(orderStore='102101')))
            querysetlist.append(queryset2.filter(Q(orderStore=102101)))
            querysetlist.append(queryset3.filter(Q(storeCode='102101')))

        elif _per == 13:
            # b2b双鸭山数据 103101
            querysetlist.append(queryset1.filter(Q(orderStore='103101')))
            querysetlist.append(queryset2.filter(Q(orderStore=103101)))
            querysetlist.append(queryset3.filter(Q(storeCode='103101')))

        elif _per == 14:
            # b2b东北数据 104101
            querysetlist.append(queryset1.filter(Q(orderStore='104101')))
            querysetlist.append(queryset2.filter(Q(orderStore=104101)))
            querysetlist.append(queryset3.filter(Q(storeCode='104101')))

        elif _per == 15:
            # b2b华南数据 105101
            querysetlist.append(queryset1.filter(Q(orderStore='105101')))
            querysetlist.append(queryset2.filter(Q(orderStore=105101)))
            querysetlist.append(queryset3.filter(Q(storeCode='105101')))


        elif _per == 16:
            # b2b西南数据 106101
            querysetlist.append(queryset1.filter(Q(orderStore='106101')))
            querysetlist.append(queryset2.filter(Q(orderStore=106101)))
            querysetlist.append(queryset3.filter(Q(storeCode='106101')))

        elif _per == 17:
            # b2b北方数据 107101
            querysetlist.append(queryset1.filter(Q(orderStore='107101')))
            querysetlist.append(queryset2.filter(Q(orderStore=107101)))
            querysetlist.append(queryset3.filter(Q(storeCode='107101')))


        elif _per == 18:
            # b2b华东数据 108101
            querysetlist.append(queryset1.filter(Q(orderStore='108101')))
            querysetlist.append(queryset2.filter(Q(orderStore=108101)))
            querysetlist.append(queryset3.filter(Q(storeCode='108101')))

        elif _per == 19:
            # b2b西北数据 109101
            querysetlist.append(queryset1.filter(Q(orderStore='109101')))
            querysetlist.append(queryset2.filter(Q(orderStore=109101)))
            querysetlist.append(queryset3.filter(Q(storeCode='109101')))


        elif _per == 20:
            # b2b中原数据 110101
            querysetlist.append(queryset1.filter(Q(orderStore='110101')))
            querysetlist.append(queryset2.filter(Q(orderStore=110101)))
            querysetlist.append(queryset3.filter(Q(storeCode='110101')))

        return querysetlist

@login_required(login_url='/login/')
def today_income(request):
    # 今日营收
    res = {}

    # 获取时间  日期
    incometd = incomeDay()
    _dtnow = incometd._get_today()        # ['2018', '05', '12', '04']

    try: # 获取 权限
        _per = incometd._get_permission(request)
    except:
        return JsonResponse({'res': '没有权限'})

    # 得到querysetlist
    queryset_list = incometd._get_queryset_list(request, _dtnow[0], _dtnow[1], _dtnow[2], _per)

    # 进一步 获取数据
    b2b_order = 0 if queryset_list[0].aggregate(Sum('amount'))['amount__sum'] == None else queryset_list[0].aggregate(Sum('amount'))['amount__sum']
    b2b_pos =  0 if queryset_list[1].aggregate(Sum('amount'))['amount__sum'] == None else queryset_list[1].aggregate(Sum('amount'))['amount__sum']

    res['order_count'] = str(len(queryset_list[0])+len(queryset_list[1])) ###################################
    res['order_amount'] = str(int(b2b_order+b2b_pos)) ###################################
    res['ordered_cust_count'] = str(len(queryset_list[0].values('memberPin').distinct())) ###################################
    res['newreg_count'] = str(len(queryset_list[2])) ###################################

    # 获取每小时数据
    res['hours_data'] = []
    for i in range(0,int(_dtnow[3])+1):
        q1 = 0 if queryset_list[0].filter(createDate__hour=i).aggregate(Sum('amount'))['amount__sum'] == None else queryset_list[0].filter(createDate__hour=i).aggregate(Sum('amount'))['amount__sum']
        q2 = 0 if queryset_list[1].filter(createDate__hour=i).aggregate(Sum('amount'))['amount__sum'] == None else queryset_list[1].filter(createDate__hour=i).aggregate(Sum('amount'))['amount__sum']
        res['hours_data'].append(int(q1 + q2))

    return JsonResponse(res)




































def income_month(request, *args):
    '''今日营收图，根据不同区域人员，展现不同数据'''
    year = args[0]
    month = args[1]

    res = {}

    # 取当月收入总和
    query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)
    query3 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)

    b2b_order = 0 if len(query1) == 0 else query1.aggregate(Sum('amount'))['amount__sum']
    b2b_pos =  0 if len(query3) == 0 else query3.aggregate(Sum('amount'))['amount__sum']

    res['order_amount_month'] = str(int(b2b_pos+b2b_order))########



    # 取上月总收入
    if month == '01':
        query2 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=str(int(year)-1), createDate__month='12')
        query4 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=str(int(year)-1), createDate__month='12')

    else:
        query2 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=str(int(month)-1))
        query4 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=str(int(month)-1))

    res['order_amount_lastmonth'] = str(int(query2.aggregate(Sum('amount'))['amount__sum']+query4.aggregate(Sum('amount'))['amount__sum']))########
    res['month_ratio'] = str(int((float(res['order_amount_month'])-float(res['order_amount_lastmonth']))/float(res['order_amount_lastmonth']) * 100))+r'%' ##########
    res['ratio'] = str(int(float(res['order_amount_month'])/float(res['order_amount_lastmonth']) * 100))+r'%'
    # 取当年总收入
    query5 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year)
    query6 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year)
    res['order_amount_year'] = str(int(query5.aggregate(Sum('amount'))['amount__sum']+query6.aggregate(Sum('amount'))['amount__sum']))########
    # 取上年总收入
    query7 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=str(int(year)-1))
    query8 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=str(int(year)-1))
    order_amount_lastyear = str(int(query7.aggregate(Sum('amount'))['amount__sum']+query8.aggregate(Sum('amount'))['amount__sum']))
    res['year_ratio'] = str(int((float(res['order_amount_year'])-float(order_amount_lastyear))/float(order_amount_lastyear) * 100))+r'%' #####
    return JsonResponse(res)




def store_count(request, *args):
    '''新增客户数'''
    year = args[0]
    month = args[1]
    res = {}
    query = b2b_storeb2b.objects.using('hzyg').filter(created_dt__year=year, created_dt__month=month) # 当月
    if month == '01':
        query1 = b2b_storeb2b.objects.using('hzyg').filter(created_dt__year=str(int(year)-1), created_dt__month=12)
    else:
        query1 = b2b_storeb2b.objects.using('hzyg').filter(created_dt__year=year, created_dt__month=str(int(month)-1))
    res['store_reg_month'] = str(len(query))
    res['store_reg_lastmonth'] = str(len(query1))
    res['ratio'] = str(int(int(res['store_reg_month'])/int(res['store_reg_lastmonth'])*100)) + '%'
    res['month_ratio'] = str(int((int(res['store_reg_month'])-int(res['store_reg_lastmonth']))/int(res['store_reg_lastmonth'])*100)) + '%'

    query2 = b2b_storeb2b.objects.using('hzyg').filter(created_dt__year=year) # 当年
    query3 = b2b_storeb2b.objects.using('hzyg').filter(created_dt__year=str(int(year)-1)) # 去年
    res['store_reg_year'] = str(len(query2))
    store_reg_lastyear = len(query3)
    res['year_ratio'] = str(int((int(res['store_reg_year'])-store_reg_lastyear)/store_reg_lastyear*100))+'%'
    return JsonResponse(res)

def ordered_store_count(request, *args):
    '''新增客户数'''
    year = args[0]
    month = args[1]
    res = {}
    query = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month) # 当月
    if month == '01':
        query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=str(int(year)-1), createDate__month=12)
    else:
        query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=str(int(month)-1))
    # 本月
    res['odstore_count_month'] = str(len(query.values('memberPin').distinct()))
    res['odstore_count_lastmonth'] = str(len(query1.values('memberPin').distinct()))
    res['ratio'] = str(int(int(res['odstore_count_month'])/int(res['odstore_count_lastmonth'])*100)) + '%'
    res['month_ratio'] = str(int((int(res['odstore_count_month'])-int(res['odstore_count_lastmonth']))/int(res['odstore_count_lastmonth'])*100)) + '%'

    query2 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year) # 当年
    query3 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=str(int(year)-1)) # 去年
    res['odstore_count_year'] = str(len(query2.values('memberPin').distinct()))
    odstore_count_lastyear = len(query3.values('memberPin').distinct())
    res['year_ratio'] = str(int((int(res['odstore_count_year'])-odstore_count_lastyear)/odstore_count_lastyear*100))+'%'
    return JsonResponse(res)


def order_count(request, *args):
    '''新增客户数'''
    year = args[0]
    month = args[1]
    res = {}
    query = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month) # 当月
    if month == '01':
        query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=str(int(year)-1), createDate__month=12)
    else:
        query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=str(int(month)-1))
    # 本月
    res['order_month'] = str(len(query))
    res['order_lastmonth'] = str(len(query1))
    res['ratio'] = str(int(int(res['order_month'])/int(res['order_lastmonth'])*100)) + '%'
    res['month_ratio'] = str(int((int(res['order_month'])-int(res['order_lastmonth']))/int(res['order_lastmonth'])*100)) + '%'

    query2 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year) # 当年
    query3 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=str(int(year)-1)) # 去年
    res['order_year'] = str(len(query2))
    order_lastyear = len(query3)
    res['year_ratio'] = str(int((int(res['order_year'])-order_lastyear)/order_lastyear*100))+'%'
    return JsonResponse(res)


def channal_salesamount_month(request, *args):
    '''本月各渠道销售额'''
    year = args[0]
    month = args[1]
    res = {}
    query = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month) # 当月
    query1 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month) # 当月

    b2b_1 = query.aggregate(Sum('amount'))['amount__sum']# all
    b2b_2 = query1.aggregate(Sum('amount'))['amount__sum'] # pos

    agriculture = query.filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单')).aggregate(Sum('amount'))['amount__sum'] # 农业
    online = query.filter(Q(orderStoreName='京东九河泉仓库') | Q(orderStoreName='京东官方直营店') | Q(orderStoreName='民生银行仓库')).aggregate(Sum('amount'))['amount__sum'] # 电商
    television = query.filter(orderStoreName='电视购物仓库').aggregate(Sum('amount'))['amount__sum']# 电视
    taste = query.filter(orderStoreName='禾中味道官方直营店').aggregate(Sum('amount'))['amount__sum']# 禾中味道
    direct_store = query.filter(orderStoreName='直营门店').aggregate(Sum('amount'))['amount__sum']# 直营店

    if agriculture == None:
        agriculture = 0
    if online == None:
        online = 0
    if television == None:
        television = 0
    if taste == None:
        taste = 0
    if direct_store == None:
        direct_store = 0
    if b2b_1 == None:
        b2b_1 = 0
    if b2b_2 == None:
        b2b_2 = 0

    b2b_all = b2b_1 - (agriculture + online + television + taste + direct_store) + b2b_2
    res['b2b'] = str(int(b2b_all))
    res['agriculture'] = str(int(agriculture))
    res['online'] = str(int(online))
    res['television'] = str(int(television))
    res['taste'] = str(int(taste))
    return JsonResponse(res)


def sales_trend(request):
    '''销售趋势'''
    pass


def classify_amount_month(request, *args):
    '''当月分类销售额'''
    pass