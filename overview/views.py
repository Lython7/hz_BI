from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q

from hzyg.models import *
from permissions.decorator import *

from .assistant import incomeDay



# @login_required(login_url='/login/')
@tdincome_which
def today_income(request):
    # 今日营收
    res = {}

    # 获取时间  日期
    incometd = incomeDay()
    _dtnow = incometd._get_today()        # ['2018', '05', '12', '04']

    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['today_income']
    except:
        return JsonResponse({'res': '没有权限'})

    # 得到querysetlist
    queryset_list = incometd._get_queryset_list(request, _dtnow[0], _dtnow[1], _dtnow[2], _settings)

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

@login_required(login_url='/login/')
@sales_amount_which
def sales_amount(request):
    # 销售额表
    res = {}

    # 获取日期
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']

    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['sales_amount']
    except:
        return JsonResponse({'res': '没有权限'})


    queryset_list_month = incometd._get_queryset_list(request, __date[0], __date[1], None, _settings)
    if __date[1] == '01':
        queryset_list_lastmonth = incometd._get_queryset_list(request, str(int(__date[0])-1), '12', None, _settings)
    else:
        queryset_list_lastmonth = incometd._get_queryset_list(request, __date[0], str(int(__date[1])-1), None, _settings)

    b2b_order = 0 if queryset_list_month[0].aggregate(Sum('amount'))['amount__sum'] == None else queryset_list_month[0].aggregate(Sum('amount'))['amount__sum']
    b2b_pos =  0 if queryset_list_month[1].aggregate(Sum('amount'))['amount__sum'] == None else queryset_list_month[1].aggregate(Sum('amount'))['amount__sum']
    res['order_amount_month'] = str(int(b2b_pos+b2b_order))########

    res['order_amount_lastmonth'] = str(int(queryset_list_lastmonth[0].aggregate(Sum('amount'))['amount__sum']+queryset_list_lastmonth[1].aggregate(Sum('amount'))['amount__sum']))########
    res['month_ratio'] = str(int((float(res['order_amount_month'])-float(res['order_amount_lastmonth']))/float(res['order_amount_lastmonth']) * 100))+r'%' ##########
    res['ratio'] = str(int(float(res['order_amount_month'])/float(res['order_amount_lastmonth']) * 100))+r'%'


    queryset_list_year = incometd._get_queryset_list(request, __date[0],None , None, _settings)
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), None, None, _settings)

    res['order_amount_year'] = str(int(queryset_list_year[0].aggregate(Sum('amount'))['amount__sum']+queryset_list_year[1].aggregate(Sum('amount'))['amount__sum']))########
    order_amount_lastyear = str(int(queryset_list_lastyear[0].aggregate(Sum('amount'))['amount__sum']+queryset_list_lastyear[1].aggregate(Sum('amount'))['amount__sum']))
    res['year_ratio'] = str(int((float(res['order_amount_year'])-float(order_amount_lastyear))/float(order_amount_lastyear) * 100))+r'%' #####

    return JsonResponse(res)

    # 新增客户数
@login_required(login_url='/login/')
@store_count_which
def store_count(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']

    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['store_count']
    except:
        return JsonResponse({'res': '没有权限'})

    # __date[0] = '05'

    queryset_list_month = incometd._get_queryset_list(request, __date[0], __date[1], None, _settings)
    if __date[1] == '01':
        queryset_list_lastmonth = incometd._get_queryset_list(request, str(int(__date[0])-1), '12', None, _settings)
    else:
        queryset_list_lastmonth = incometd._get_queryset_list(request, __date[0], str(int(__date[1])-1), None, _settings)
    res['store_reg_month'] = str(len(queryset_list_month[2]))
    res['store_reg_lastmonth'] = str(len(queryset_list_lastmonth[2]))
    res['ratio'] = str(int(int(res['store_reg_month'])/int(res['store_reg_lastmonth'])*100)) + '%'
    res['month_ratio'] = str(int((int(res['store_reg_month'])-int(res['store_reg_lastmonth']))/int(res['store_reg_lastmonth'])*100)) + '%'

    queryset_list_year = incometd._get_queryset_list(request, __date[0],None , None, _settings)
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), None, None, _settings)
    res['store_reg_year'] = str(len(queryset_list_year[2]))
    store_reg_lastyear = len(queryset_list_lastyear[2])
    res['year_ratio'] = str(int((int(res['store_reg_year'])-store_reg_lastyear)/store_reg_lastyear*100))+'%'

    return JsonResponse(res)


    # 下单客户数
@login_required(login_url='/login/')
@orderstore_count_which
def orderstore_count(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']

    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['orderstore_count']
    except:
        return JsonResponse({'res': '没有权限'})

    queryset_list_month = incometd._get_queryset_list(request, __date[0], __date[1], None, _settings)
    if __date[1] == '01':
        queryset_list_lastmonth = incometd._get_queryset_list(request, str(int(__date[0])-1), '12', None, _settings)
    else:
        queryset_list_lastmonth = incometd._get_queryset_list(request, __date[0], str(int(__date[1])-1), None, _settings)

    queryset_list_year = incometd._get_queryset_list(request, __date[0],None , None, _settings)
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), None, None, _settings)

    res['odstore_count_month'] = str(len(queryset_list_month[0].values('memberPin').distinct()))
    res['odstore_count_lastmonth'] = str(len(queryset_list_lastmonth[0].values('memberPin').distinct()))
    res['ratio'] = str(int(int(res['odstore_count_month'])/int(res['odstore_count_lastmonth'])*100)) + '%'
    res['month_ratio'] = str(int((int(res['odstore_count_month'])-int(res['odstore_count_lastmonth']))/int(res['odstore_count_lastmonth'])*100)) + '%'

    res['odstore_count_year'] = str(len(queryset_list_year[0].values('memberPin').distinct()))
    odstore_count_lastyear = len(queryset_list_lastyear[0].values('memberPin').distinct())
    res['year_ratio'] = str(int((int(res['odstore_count_year'])-odstore_count_lastyear)/odstore_count_lastyear*100))+'%'

    return JsonResponse(res)

    # 订单数量
@login_required(login_url='/login/')
@order_count_which
def order_count(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']

    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['order_count']
    except:
        return JsonResponse({'res': '没有权限'})

    queryset_list_month = incometd._get_queryset_list(request, __date[0], __date[1], None, _settings)
    if __date[1] == '01':
        queryset_list_lastmonth = incometd._get_queryset_list(request, str(int(__date[0])-1), '12', None, _settings)
    else:
        queryset_list_lastmonth = incometd._get_queryset_list(request, __date[0], str(int(__date[1])-1), None, _settings)

    queryset_list_year = incometd._get_queryset_list(request, __date[0],None , None, _settings)
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), None, None, _settings)

    res['order_month'] = str(len(queryset_list_month[0]))
    res['order_lastmonth'] = str(len(queryset_list_lastmonth[0]))
    res['ratio'] = str(int(int(res['order_month'])/int(res['order_lastmonth'])*100)) + '%'
    res['month_ratio'] = str(int((int(res['order_month'])-int(res['order_lastmonth']))/int(res['order_lastmonth'])*100)) + '%'

    res['order_year'] = str(len(queryset_list_year[0]))
    order_lastyear = len(queryset_list_lastyear[0])
    res['year_ratio'] = str(int((int(res['order_year'])-order_lastyear)/order_lastyear*100))+'%'
    return JsonResponse(res)



# 本月各渠道销售额
@login_required(login_url='/login/')
@channal_salesamount_month_which
def channal_salesamount_month(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']
    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['channal_salesamount_month']
    except:
        return JsonResponse({'res': '没有权限'})

    queryset_list_month = incometd._get_queryset_list(request, __date[0], __date[1], None, _settings)

    b2b_1 = queryset_list_month[0].aggregate(Sum('amount'))['amount__sum']# all
    b2b_2 = queryset_list_month[1].aggregate(Sum('amount'))['amount__sum'] # pos


    agriculture = queryset_list_month[0].filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单')).aggregate(Sum('amount'))['amount__sum'] # 农业
    online = queryset_list_month[0].filter(Q(orderStoreName='京东九河泉仓库') | Q(orderStoreName='京东官方直营店') | Q(orderStoreName='民生银行仓库')).aggregate(Sum('amount'))['amount__sum'] # 电商
    television = queryset_list_month[0].filter(orderStoreName='电视购物仓库').aggregate(Sum('amount'))['amount__sum']# 电视
    taste = queryset_list_month[0].filter(orderStoreName='禾中味道官方直营店').aggregate(Sum('amount'))['amount__sum']# 禾中味道
    direct_store = queryset_list_month[0].filter(orderStoreName='直营门店').aggregate(Sum('amount'))['amount__sum']# 直营店

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


@login_required(login_url='/login/')
@sales_trend_which
def sales_trend(request):
    '''销售趋势'''
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']
    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['channal_salesamount_month']
    except:
        return JsonResponse({'res': '没有权限'})

    queryset_list_month = incometd._get_queryset_list(request, __date[0], __date[1], None, _settings)
    tmp_ls = []
    tmp_ls.append(queryset_list_month)
    while len(tmp_ls) < 12:
        month_l = int(__date[1])
        if month_l-1 > 0:
            tmp_ls.append(incometd._get_queryset_list(request, __date[0], str(month_l-1), None, _settings))
        else:
            month_l=13
            __date[0] = str(int(__date[0])-1)
            # tmp_ls.append(incometd._get_queryset_list(request, str(int(__date[0])-1), str(int(__date[1])-1), None, _settings))

        month_l = month_l - 1

    for tmp in tmp_ls:
        pass





def classify_amount_month(request, *args):
    '''当月分类销售额'''
    pass