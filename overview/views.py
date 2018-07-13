import json
import operator

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q, Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from hz_BI.settings import CACHE_TIME
from hzyg.models import *
from investment.models import sale_upload
from permissions.decorator import *
from collections import Counter
from .assistant import incomeDay

def ranking(request):
    return render(request, 'index/ranking.html', context={})

@login_required
def goodscount(request):
    return render(request, 'index/goodscount.html', context={})

# @cache_page(CACHE_TIME)
@login_required(login_url='/login/')
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

    res['order_count'] = str(len(queryset_list[0])+len(queryset_list[1].values('orderNo').distinct())) ###################################
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

@cache_page(CACHE_TIME)
@login_required(login_url='/login/')
@sales_amount_which
def sales_amount(request):
    # 销售额表
    res = {}

    # 获取日期
    incometd = incomeDay()
    __date = incometd._get_today()        # ['2018', '05']

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



    try:
        res['order_amount_lastmonth_part'] = str(int(
            queryset_list_lastmonth[0].filter(createDate__day__gte='01', createDate__day__lte=__date[2]).aggregate(
                Sum('amount'))['amount__sum'] +
            queryset_list_lastmonth[1].filter(createDate__day__gte='01', createDate__day__lte=__date[2]).aggregate(
                Sum('amount'))['amount__sum']))  ########
    except:
        res['order_amount_lastmonth_part'] = '0'


    queryset_list_year = incometd._get_queryset_list(request, __date[0],None , None, _settings)
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), __date[1], None, _settings)

    res['order_amount_year'] = str(int(queryset_list_year[0].aggregate(Sum('amount'))['amount__sum']+queryset_list_year[1].aggregate(Sum('amount'))['amount__sum']))########
    try:
        order_amount_lastyear = str(int(queryset_list_lastyear[0].filter(createDate__day__gte='01', createDate__day__lte=__date[2]).aggregate(Sum('amount'))['amount__sum']+queryset_list_lastyear[1].filter(createDate__day__gte='01', createDate__day__lte=__date[2]).aggregate(Sum('amount'))['amount__sum']))
    except:
        order_amount_lastyear = '0'

    if float(res['order_amount_lastmonth']) == 0:
        res['ratio'] = 'N/A'
    else:
        res['ratio'] = str(int(float(res['order_amount_month']) / float(res['order_amount_lastmonth']) * 100)) + r'%'

    if float(res['order_amount_lastmonth_part']) == 0:
        res['month_ratio'] = 'N/A'
    else:
        res['month_ratio'] = str(int((float(res['order_amount_month']) - float(res['order_amount_lastmonth_part'])) / float(
            res['order_amount_lastmonth_part']) * 100)) + r'%'  ##########

    if float(order_amount_lastyear) == 0:
        res['year_ratio'] = 'N/A'
    else:
        res['year_ratio'] = str(int((float(res['order_amount_month'])-float(order_amount_lastyear))/float(order_amount_lastyear) * 100))+r'%' #####

    return JsonResponse(res)


    # 新增客户数
@cache_page(CACHE_TIME)
@login_required(login_url='/login/')
@store_count_which
def store_count(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_today()        # ['2018', '05']

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


    try:
        res['store_reg_lastmonth_part'] = str(len(queryset_list_lastmonth[2].filter(createDate__day__gte='01', createDate__day__lte=__date[2])))########
    except:
        res['store_reg_lastmonth_part'] = '0'


    queryset_list_year = incometd._get_queryset_list(request, __date[0],None , None, _settings)

    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), __date[1], None, _settings)
    res['store_reg_year'] = str(len(queryset_list_year[2]))
    try:
        store_reg_lastyear = len(queryset_list_lastyear[2])
    except:
        store_reg_lastyear = 0
    if float(int(res['store_reg_lastmonth'])) == 0:
        res['ratio'] = 'N/A'
    else:
        res['ratio'] = str(int(int(res['store_reg_month']) / int(res['store_reg_lastmonth']) * 100)) + '%'
    if float(int(res['store_reg_lastmonth_part'])) == 0:
        res['month_ratio'] = 'N/A'
    else:
        res['month_ratio'] = str(int((int(res['store_reg_month']) - int(res['store_reg_lastmonth_part'])) / int(
            res['store_reg_lastmonth_part']) * 100)) + '%'
    if store_reg_lastyear == 0:
        res['year_ratio'] = 'N/A'
    else:
        res['year_ratio'] = str(int((int(res['store_reg_month'])-store_reg_lastyear)/store_reg_lastyear*100))+'%'

    return JsonResponse(res)


    # 下单客户数
@cache_page(CACHE_TIME)
@login_required(login_url='/login/')
@orderstore_count_which
def orderstore_count(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_today()        # ['2018', '05']

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
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), __date[1], None, _settings)

    res['odstore_count_month'] = str(len(queryset_list_month[0].values('memberPin').distinct()))
    res['odstore_count_lastmonth'] = str(len(queryset_list_lastmonth[0].values('memberPin').distinct()))


    try:
        res['odstore_count_lastmonth_part'] = str(len(queryset_list_lastmonth[0].filter(createDate__day__gte='01', createDate__day__lte=__date[2]).values('memberPin').distinct()))########
    except:
        res['odstore_count_lastmonth_part'] = '0'


    res['odstore_count_year'] = str(len(queryset_list_year[0].values('memberPin').distinct()))
    try:
        odstore_count_lastyear = len(queryset_list_lastyear[0].values('memberPin').distinct())
    except:
        odstore_count_lastyear= 0

    if int(res['odstore_count_lastmonth']) == 0:
        res['ratio'] = 'N/A'
    else:
        res['ratio'] = str(int(int(res['odstore_count_month'])/int(res['odstore_count_lastmonth'])*100)) + '%'

    if int(res['odstore_count_lastmonth_part']) == 0:
        res['month_ratio'] = 'N/A'
    else:
        res['month_ratio'] = str(int((int(res['odstore_count_month']) - int(res['odstore_count_lastmonth_part'])) / int(res['odstore_count_lastmonth_part']) * 100)) + '%'

    if odstore_count_lastyear == 0:
        res['year_ratio'] = 'N/A'
    else:
        res['year_ratio'] = str(int((int(res['odstore_count_month'])-odstore_count_lastyear)/odstore_count_lastyear*100))+'%'

    return JsonResponse(res)


    # 订单数量
@cache_page(CACHE_TIME)
@login_required(login_url='/login/')
@order_count_which
def order_count(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_today()        # ['2018', '05']

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
    queryset_list_lastyear = incometd._get_queryset_list(request, str(int(__date[0])-1), __date[1], None, _settings)

    res['order_month'] = str(len(queryset_list_month[0]))
    res['order_lastmonth'] = str(len(queryset_list_lastmonth[0]))


    try:
        res['order_lastmonth_part'] = str(len(queryset_list_lastmonth[0].filter(createDate__day__gte='01', createDate__day__lte=__date[2])))########
    except:
        res['order_lastmonth_part'] = '0'


    res['order_year'] = str(len(queryset_list_year[0]))
    try:
        order_lastyear = len(queryset_list_lastyear[0])
    except:
        order_lastyear = 0

    if int(res['order_lastmonth']) == 0:
        res['ratio'] = 'N/A'
    else:
        res['ratio'] = str(int(int(res['order_month']) / int(res['order_lastmonth']) * 100)) + '%'
    if int(res['order_lastmonth_part']) == 0:
        res['month_ratio'] = 'N/A'
    else:
        res['month_ratio'] = str(int((int(res['order_month']) - int(res['order_lastmonth_part'])) / int(res['order_lastmonth_part']) * 100)) + '%'
    if order_lastyear == 0:
        res['year_ratio'] = 'N/A'
    else:
        res['year_ratio'] = str(int((int(res['order_month'])-order_lastyear)/order_lastyear*100))+'%'
    return JsonResponse(res)



# 本月各渠道销售额
@cache_page(CACHE_TIME)
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


    b2c = b2b_posgoods.objects.using('hzyg').filter(createDate__year=__date[0], createDate__month=__date[1],).aggregate(Sum('amount'))['amount__sum']

    agriculture = queryset_list_month[0].filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单')).aggregate(Sum('amount'))['amount__sum'] # 农业
    online = queryset_list_month[0].filter(Q(orderStoreName='京东九河泉仓库') | Q(orderStoreName='京东官方直营店') | Q(orderStoreName='民生银行仓库')).aggregate(Sum('amount'))['amount__sum'] # 电商
    television = queryset_list_month[0].filter(orderStoreName='电视购物仓库').aggregate(Sum('amount'))['amount__sum']# 电视
    taste = queryset_list_month[0].filter(orderStoreName='禾中味道官方直营店').aggregate(Sum('amount'))['amount__sum']# 禾中味道
    direct_store = queryset_list_month[0].filter(orderStoreName='直营门店').aggregate(Sum('amount'))['amount__sum']# 直营店
    chanpinbu = b2b_ordertable.objects.using('hzyg').filter(createDate__year=__date[0], createDate__month=__date[1],orderStoreName='产品部仓库').aggregate(Sum('amount'))['amount__sum']

    if agriculture == None:
        agriculture = 0
    if online == None:
        online = 0
    if television == None:
        television = 0
    if b2c == None:
        b2c = 0
    if chanpinbu == None:
        chanpinbu = 0
    if b2b_1 == None:
        b2b_1 = 0
    if b2b_2 == None:
        b2b_2 = 0

    if taste == None:
        taste = 0
    if direct_store == None:
        direct_store =0


    b2b_all = b2b_1 - (agriculture + online + television + taste + direct_store) + b2b_2
    res['b2b'] = str(int(b2b_all))
    res['b2c'] = str(int(b2c))
    res['agriculture'] = str(int(agriculture))
    res['online'] = str(int(online))
    res['television'] = str(int(television))
    res['chanpinbu'] = str(int(chanpinbu))
    return JsonResponse(res)

# 销售趋势
@cache_page(CACHE_TIME)
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
    month_l = int(__date[1])

    date_ls = []
    date_ls.append(str(__date[0][2::])+'.'+str(month_l))
    while len(tmp_ls) < 12:

        if month_l-1 > 0:
            tmp_ls.append(incometd._get_queryset_list(request, __date[0], str(month_l-1), None, _settings))
            date_ls.append(str(__date[0][2::])+'.'+str(month_l-1))
        else:
            month_l=14
            __date[0] = str(int(__date[0])-1)
            # tmp_ls.append(incometd._get_queryset_list(request, str(int(__date[0])-1), str(int(__date[1])-1), None, _settings))

        month_l = month_l - 1

    data = []
    for tmp in tmp_ls:
        b2b_order = 0 if tmp[0].aggregate(Sum('amount'))['amount__sum'] == None else tmp[0].aggregate(Sum('amount'))['amount__sum']
        b2b_pos =  0 if tmp[1].aggregate(Sum('amount'))['amount__sum'] == None else tmp[1].aggregate(Sum('amount'))['amount__sum']

        data.append(int(b2b_pos+b2b_order))

    res['data'] = data[::-1]
    res['date'] = date_ls[::-1]

    # res = dict(zip(date_ls, data))
    return JsonResponse(res)



# @cache_page(CACHE_TIME)
@login_required(login_url='/login/')
@classify_amount_month_which
def classify_amount_month(request):
    '''当月分类销售额'''
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']
    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['channal_salesamount_month']
    except:
        return JsonResponse({'res': '没有权限'})

    classify_data_goods = list(b2b_goodstable.objects.using('hzyg').filter(createDate__year=__date[0], createDate__month=__date[1]).values('secondIcatName').annotate(Sum('amount')))
    classify_data_pos = list(b2b_posgoods.objects.using('hzyg').filter(createDate__year=__date[0], createDate__month=__date[1]).values('secondIcatName').annotate(Sum('amount')))


    data_dict_goods = {}
    for i in classify_data_goods:
        data_dict_goods[i['secondIcatName']] = int(i['amount__sum'])

    data_dict_pos = {}
    for i in  classify_data_pos:
        data_dict_pos[i['secondIcatName']] = int(i['amount__sum'])

    X, Y = Counter(data_dict_goods), Counter(data_dict_pos)

    res['data'] = dict(X + Y)

    return JsonResponse(res)


# @cache_page(CACHE_TIME)
def goodscount_2(request):
    if request.method == 'GET':
        res = {}

        incometd = incomeDay()
        date_list = incometd._get_today()
        try:
            classify = request.GET.get('classify', None)
        except:
            classify = None
        if classify == None:
            return JsonResponse({'res':'no classify'})
        lyear = int(request.GET.get('lyear', date_list[0]))
        lmonth = int(request.GET.get('lmonth', date_list[1]))
        lday = int(request.GET.get('lday', '1'))
        ryear = int(request.GET.get('ryear', date_list[0]))
        rmonth = int(request.GET.get('rmonth', date_list[1]))
        rday = int(request.GET.get('rday', date_list[2]))


        queryset_pos =  b2b_posgoods.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
                                                                  createDate__lte=datetime(ryear, rmonth, rday),
                                                                  secondIcatName=classify,
                                                                  )
        queryset_goodstb = b2b_goodstable.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
                                                                       createDate__lte=datetime(ryear, rmonth, rday),
                                                                       secondIcatName=classify,
                                                                       )


        data_pos = queryset_pos.values('skuName').annotate(Sum('amount'))

        data_goodstb = queryset_goodstb.values('skuName').annotate(Sum('amount'))

        # count_pos = queryset_pos.aggregate(Sum('skuNum'))
        # count_goodstb = queryset_goodstb.aggregate(Sum('skuNum'))
        # print(count_pos)

        if classify == None:
            return JsonResponse({'res': 'failed'})

        goodstb_dic = {}
        pos_dic = {}
        try:
            for data in list(data_goodstb):
                # goodstb_ls.append({data['skuName'] : int(data['amount__sum'])})
                goodstb_dic[data['skuName']] = data['amount__sum']
        except:
            pass
        try:
            for data1 in list(data_pos):
                pos_dic[data1['skuName']] = data1['amount__sum']
        except:
            pass

        X, Y = Counter(goodstb_dic), Counter(pos_dic)
        Z = dict(X + Y)
        ret = sorted(Z.items(),key = lambda x:x[1],reverse = True)

        # print(ret)

        recvs = {}
        for i in range(len(ret[0:5])):
            recvs[ret[i][0]] = int(ret[i][1])
        print(recvs)
        sums = 0
        for i in recvs.values():
            sums = sums + i
        print(sums)
        recv = {}
        for i in range(len(ret)):
            recv[ret[i][0]] = ret[i][1]
        print(recv)

        sum = 0
        for i in recv.values():
            sum = sum + i
        print(sum)
        recvs['其它'] = int(sum) - int(sums)
        res['amount'] = int(sum)
        res['data'] = recvs
        # res['count'] = int(count_pos['skuNum__sum'])+int(count_goodstb['skuNum__sum'])

        return JsonResponse(res)

# 本月区域销售额
@cache_page(CACHE_TIME)
@login_required(login_url='/login/')
@area_salesamount_month_which
def region_amount_month(request):
    res = {}
    incometd = incomeDay()
    __date = incometd._get_month()        # ['2018', '05']
    try: # 获取 显示哪个
        _settings = incometd._get_settings(request)['channal_salesamount_month']
    except:
        return JsonResponse({'res': '没有权限'})

    # classify_data = b2b_goodstable.objects.using('hzyg').filter(createDate__year=__date[0], createDate__month=__date[1]).values('secondIcatName').annotate(Sum('amount'))
    #
    # res['data'] = list(classify_data)
    dianshang = incometd._get_queryset_list(request, __date[0], __date[1], None, 2)
    dianshang_order = 0 if dianshang[0].aggregate(Sum('amount'))['amount__sum'] == None else dianshang[0].aggregate(Sum('amount'))['amount__sum']
    dianshang_pos =  0 if dianshang[1].aggregate(Sum('amount'))['amount__sum'] == None else dianshang[1].aggregate(Sum('amount'))['amount__sum']
    res['电商渠道'] = int(dianshang_order+dianshang_pos)########

    dianshi = incometd._get_queryset_list(request, __date[0], __date[1], None, 3)
    dianshi_order = 0 if dianshi[0].aggregate(Sum('amount'))['amount__sum'] == None else dianshi[0].aggregate(Sum('amount'))['amount__sum']
    dianshi_pos =  0 if dianshi[1].aggregate(Sum('amount'))['amount__sum'] == None else dianshi[1].aggregate(Sum('amount'))['amount__sum']
    res['电视购物'] = int(dianshi_order+dianshi_pos)########

    b2bbeijing = incometd._get_queryset_list(request, __date[0], __date[1], None, 5)
    b2bbeijing_order = 0 if b2bbeijing[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bbeijing[0].aggregate(Sum('amount'))['amount__sum']
    b2bbeijing_pos =  0 if b2bbeijing[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bbeijing[1].aggregate(Sum('amount'))['amount__sum']
    res['北京区域'] = int(b2bbeijing_order+b2bbeijing_pos)########


    b2bhuabei = incometd._get_queryset_list(request, __date[0], __date[1], None, 6)
    b2bhuabei_order = 0 if b2bhuabei[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bhuabei[0].aggregate(Sum('amount'))['amount__sum']
    b2bhuabei_pos =  0 if b2bhuabei[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bhuabei[1].aggregate(Sum('amount'))['amount__sum']
    res['华北大区'] = int(b2bhuabei_order+b2bhuabei_pos)########

    b2bshuangyashan = incometd._get_queryset_list(request, __date[0], __date[1], None, 7)
    b2bshuangyashan_order = 0 if b2bshuangyashan[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bshuangyashan[0].aggregate(Sum('amount'))['amount__sum']
    b2bshuangyashan_pos =  0 if b2bshuangyashan[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bshuangyashan[1].aggregate(Sum('amount'))['amount__sum']
    res['双鸭山区域'] = int(b2bshuangyashan_order+b2bshuangyashan_pos)########

    b2bdongbei = incometd._get_queryset_list(request, __date[0], __date[1], None, 8)
    b2bdongbei_order = 0 if b2bdongbei[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bdongbei[0].aggregate(Sum('amount'))['amount__sum']
    b2bdongbei_pos =  0 if b2bdongbei[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bdongbei[1].aggregate(Sum('amount'))['amount__sum']
    res['东北大区'] = int(b2bdongbei_order+b2bdongbei_pos)########

    b2bhuanan = incometd._get_queryset_list(request, __date[0], __date[1], None, 9)
    b2bhuanan_order = 0 if b2bhuanan[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bhuanan[0].aggregate(Sum('amount'))['amount__sum']
    b2bhuanan_pos =  0 if b2bhuanan[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bhuanan[1].aggregate(Sum('amount'))['amount__sum']
    res['华南大区'] = int(b2bhuanan_order+b2bhuanan_pos)########

    b2bxinan = incometd._get_queryset_list(request, __date[0], __date[1], None, 10)
    b2bxinan_order = 0 if b2bxinan[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bxinan[0].aggregate(Sum('amount'))['amount__sum']
    b2bxinan_pos =  0 if b2bxinan[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bxinan[1].aggregate(Sum('amount'))['amount__sum']
    res['西南大区'] = int(b2bxinan_order+b2bxinan_pos)########

    b2bbeifang = incometd._get_queryset_list(request, __date[0], __date[1], None, 11)
    b2bbeifang_order = 0 if b2bbeifang[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bbeifang[0].aggregate(Sum('amount'))['amount__sum']
    b2bbeifang_pos =  0 if b2bbeifang[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bbeifang[1].aggregate(Sum('amount'))['amount__sum']
    res['北方大区'] = int(b2bbeifang_order+b2bbeifang_pos)########

    b2bhuadong = incometd._get_queryset_list(request, __date[0], __date[1], None, 12)
    b2bhuadong_order = 0 if b2bhuadong[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bhuadong[0].aggregate(Sum('amount'))['amount__sum']
    b2bhuadong_pos =  0 if b2bhuadong[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bhuadong[1].aggregate(Sum('amount'))['amount__sum']
    res['华东大区'] = int(b2bhuadong_order+b2bhuadong_pos)########

    b2bxibei = incometd._get_queryset_list(request, __date[0], __date[1], None, 13)
    b2bxibei_order = 0 if b2bxibei[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bxibei[0].aggregate(Sum('amount'))['amount__sum']
    b2bxibei_pos =  0 if b2bxibei[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bxibei[1].aggregate(Sum('amount'))['amount__sum']
    res['西北大区'] = int(b2bxibei_order+b2bxibei_pos)########

    b2bzhongyuan = incometd._get_queryset_list(request, __date[0], __date[1], None, 14)
    b2bzhongyuan_order = 0 if b2bzhongyuan[0].aggregate(Sum('amount'))['amount__sum'] == None else b2bzhongyuan[0].aggregate(Sum('amount'))['amount__sum']
    b2bzhongyuan_pos =  0 if b2bzhongyuan[1].aggregate(Sum('amount'))['amount__sum'] == None else b2bzhongyuan[1].aggregate(Sum('amount'))['amount__sum']
    res['中原大区'] = int(b2bzhongyuan_order+b2bzhongyuan_pos)########

    # zhiyingdian = incometd._get_queryset_list(request, __date[0], __date[1], None, 15)
    # zhiyingdian_order = 0 if zhiyingdian[0].aggregate(Sum('amount'))['amount__sum'] == None else zhiyingdian[0].aggregate(Sum('amount'))['amount__sum']
    # zhiyingdian_pos =  0 if zhiyingdian[1].aggregate(Sum('amount'))['amount__sum'] == None else zhiyingdian[1].aggregate(Sum('amount'))['amount__sum']
    # res['直营店'] = int(zhiyingdian_order+zhiyingdian_pos)########

    hezhongnongye = incometd._get_queryset_list(request, __date[0], __date[1], None, 16)
    hezhongnongye_order = 0 if hezhongnongye[0].aggregate(Sum('amount'))['amount__sum'] == None else hezhongnongye[0].aggregate(Sum('amount'))['amount__sum']
    hezhongnongye_pos =  0 if hezhongnongye[1].aggregate(Sum('amount'))['amount__sum'] == None else hezhongnongye[1].aggregate(Sum('amount'))['amount__sum']
    res['禾中农业'] = int(hezhongnongye_order+hezhongnongye_pos)########

    # hezhongweidao = incometd._get_queryset_list(request, __date[0], __date[1], None, 17)
    # hezhongweidao_order = 0 if hezhongweidao[0].aggregate(Sum('amount'))['amount__sum'] == None else hezhongweidao[0].aggregate(Sum('amount'))['amount__sum']
    # hezhongweidao_pos =  0 if hezhongweidao[1].aggregate(Sum('amount'))['amount__sum'] == None else hezhongweidao[1].aggregate(Sum('amount'))['amount__sum']
    # res['禾中味道'] = int(hezhongweidao_order+hezhongweidao_pos)########

    chanpinbu = incometd._get_queryset_list(request, __date[0], __date[1], None, 18)
    chanpinbu_order = 0 if chanpinbu[0].aggregate(Sum('amount'))['amount__sum'] == None else chanpinbu[0].aggregate(Sum('amount'))['amount__sum']
    chanpinbu_pos =  0 if chanpinbu[1].aggregate(Sum('amount'))['amount__sum'] == None else chanpinbu[1].aggregate(Sum('amount'))['amount__sum']
    res['产品部'] = int(chanpinbu_order+chanpinbu_pos)########

    ret = sorted(res.items(),key = lambda x:x[1],reverse = True)
    # return HttpResponse(ret)
    recv = {}
    for i in range(len(ret)):
        recv[ret[i][0]] = ret[i][1]
        # recv[ret[1][0]] = ret[1][1]
        # recv[ret[2][0]] = ret[2][1]
    return JsonResponse(recv)

# 本月B2B销售人员TOP3
# @login_required(login_url='/login/')
# @B2B_TOP3_month_which
# def b2b_top3_month(request):
#     pass
#

# @cache_page(CACHE_TIME)
def score(request, year, month):
    '''
        业务员数据API  hzyg备份数据库  和 excel读取汇总
    '''
    queryset = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year,createDate__month=month).filter(orderStore='101101').filter(amount__gt=0)
    queryset_investment = sale_upload.objects.using('investment').filter(createdate__year=year, createdate__month=month).filter(checkif=1)
    mysqldata = queryset.values('realName').annotate(c=Count('amount'),s=Sum('amount')).values_list('realName','c','s').order_by('-s')
    # if queryset_investment.
    mysqldata_investment = queryset_investment.values('salesname').annotate(c=Count('amount'), s=Sum('amount')).values_list('salesname','c', 's')
    datalist = []
    # datalist_investment = []


    for data in mysqldata:
        datalist.append({'name': data[0],'count': data[1], 'sum': data[2]})
    try:
        for dt in mysqldata_investment:
            # print(data)
            tmp_dic = {'name': dt[0],'count': dt[1], 'sum': dt[2]}
            datalist.append(tmp_dic)
    except:
        pass

    keyforname = []
    dataend = []
    try:
        for datanum in range(len(datalist)):

            if str(datalist[datanum]['name']) not in keyforname:
                keyforname.append(datalist[datanum]['name'])
                dataend.append(datalist[datanum])

            else:
                for index in range(len(datalist)):
                    if index < datanum and datalist[index]['name'] == datalist[datanum]['name']:
                        dataend[index]['count'] = datalist[index]['count']+datalist[datanum]['count']
                        dataend[index]['sum'] = datalist[index]['sum']+datalist[datanum]['sum']
                        break
        dataend_sort = sorted(dataend, key=operator.itemgetter('sum'), reverse=True)


        for x in datalist:
            x['sum'] = str(x['sum'])

        return HttpResponse(json.dumps(dataend_sort), content_type='application/json')
    except:
        return HttpResponse(json.dumps({'result': 'faild lianxiguanliyuan'}), content_type='application/json')





