from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from hzyg.models import *


def income(request, *args):
    '''今日营收图，根据不同区域人员，展现不同数据'''
    year = args[0]
    month = args[1]
    day = args[2]
    if args[3] == '':
        hour = 23
    else:
        hour = int(args[3])
    res = {}
    # date = year + '-' +month + '-' + day
    if day == '':
        if month == '':
            # 取当年收入总和
            pass

        else:
            # 取当月收入总和
            query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)
            query3 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)
            res['order_amount_month'] = str(int(query1.aggregate(Sum('amount'))['amount__sum']+query3.aggregate(Sum('amount'))['amount__sum']))########
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

    else:
        # 取当日收入总和
        query1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)
        query3 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)
        res['order_count'] = str(len(query1)+len(query3)) ###################################
        res['order_amount'] = str(int(query1.aggregate(Sum('amount'))['amount__sum']+query3.aggregate(Sum('amount'))['amount__sum'])) ###################################
        res['ordered_cust_count'] = str(len(query1.values('memberPin').distinct())) ###################################

        query2 = b2b_storeb2b.objects.using('hzyg').filter(created_dt__year=year, created_dt__month=month, created_dt__day=day)
        res['newreg_count'] = str(len(query2)) ###################################
        print(res)
        # 获取每小时数据
        res['hours_data'] = []
        for i in range(0,hour+1):
            q1 = query1.filter(createDate__hour=i).aggregate(Sum('amount'))['amount__sum']
            q2 = query3.filter(createDate__hour=i).aggregate(Sum('amount'))['amount__sum']
            if q1 == None:
                q1 = 0
            if q2 == None:
                q2 = 0
            res['hours_data'].append(int(q1 + q2))

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

