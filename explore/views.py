from collections import Counter
from datetime import datetime, timedelta
import time
from time import strftime
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.shortcuts import render
from hzyg.models import *


def make_time(year, month, day):
    __time = str(year) + '-' + str(month) + '-' + str(day)
    timeArray = time.strptime(__time, "%Y-%m-%d")
    return int(time.mktime(timeArray))

def getEveryHour(begin_date,end_date):
    hour_list = []
    begin_date = datetime.strptime(begin_date, "%Y-%m-%d %H")
    end_date = datetime.strptime(end_date,"%Y-%m-%d %H")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d %H")
        hour_list.append(date_str)
        begin_date += timedelta(hours=1)
    return hour_list

def getEveryDay(begin_date,end_date):
    hour_list = []
    begin_date = datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        hour_list.append(date_str)
        begin_date += timedelta(1)
    return hour_list

# Create your views here.
from overview.assistant import incomeDay


def explore(request):
    return render(request, 'explore/explore.html', context={})



def explore_API(request):
    res = {}

    incometd = incomeDay()
    date_list = incometd._get_today()

    channal = request.GET.get('channal', '全部渠道')
    region = request.GET.get('region', '全部区域')
    depot = request.GET.get('depot', '全部配送中心')

    lyear = int(request.GET.get('lyear', date_list[0]))
    lmonth = int(request.GET.get('lmonth', date_list[1]))
    lday = int(request.GET.get('lday', '1'))
    ryear = int(request.GET.get('ryear', date_list[0]))
    rmonth = int(request.GET.get('rmonth', date_list[1]))
    rday = int(request.GET.get('rday', date_list[2]))
    # print(rday)

    queryset_1 = b2b_ordertable.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday), createDate__lte=datetime(ryear, rmonth, rday, 23, 59 ,59))
    queryset_2 = b2b_posgoods.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday), createDate__lte=datetime(ryear, rmonth, rday, 23, 59 ,59))
    queryset_3 = b2b_store.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday), createDate__lte=datetime(ryear, rmonth, rday, 23, 59 ,59))
    queryset_4 = b2b_goodstable.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday), createDate__lte=datetime(ryear, rmonth, rday, 23, 59 ,59))

    if channal == '全部渠道' and region == '全部区域' and depot == '全部配送中心':
        queryset_order = queryset_1
        queryset_pos = queryset_2
        queryset_store = queryset_3
        queryset_goods = queryset_4

    elif channal == 'B2B' and region == '全部区域' and depot == '全部配送中心':
        queryset_order = queryset_1.filter(Q(orderStoreName='北京仓库') |
                                            Q(orderStoreName='北京分仓') |
                                            Q(orderStoreName='天津仓库') |
                                            Q(orderStoreName='双鸭山仓库') |
                                            Q(orderStoreName='沈阳仓库') |
                                            Q(orderStoreName='深圳仓库') |
                                            Q(orderStoreName='成都仓库') |
                                            Q(orderStoreName='呼和浩特仓库') |
                                            Q(orderStoreName='上海仓库') |
                                            Q(orderStoreName='兰州仓库') |
                                            Q(orderStoreName='郑州仓库'))
        queryset_goods = queryset_4.filter(Q(orderStoreName='北京仓库') |
                                           Q(orderStoreName='北京分仓') |
                                           Q(orderStoreName='天津仓库') |
                                           Q(orderStoreName='双鸭山仓库') |
                                           Q(orderStoreName='沈阳仓库') |
                                           Q(orderStoreName='深圳仓库') |
                                           Q(orderStoreName='成都仓库') |
                                           Q(orderStoreName='呼和浩特仓库') |
                                           Q(orderStoreName='上海仓库') |
                                           Q(orderStoreName='兰州仓库') |
                                           Q(orderStoreName='郑州仓库'))

        queryset_pos = None
        queryset_store = queryset_3.filter(Q(storeName='北京仓库') |
                                           Q(storeName='北京分仓') |
                                           Q(storeName='天津仓库') |
                                           Q(storeName='双鸭山仓库') |
                                           Q(storeName='沈阳仓库') |
                                           Q(storeName='深圳仓库') |
                                           Q(storeName='成都仓库') |
                                           Q(storeName='呼和浩特仓库') |
                                           Q(storeName='上海仓库') |
                                           Q(storeName='兰州仓库') |
                                           Q(storeName='郑州仓库'))

    elif channal == 'B2B' and region == '总部机构' and depot == '全部配送中心':
        queryset_order = queryset_1.filter(Q(orderStoreName='北京仓库') | Q(orderStoreName='北京分仓'))
        queryset_goods = queryset_4.filter(Q(orderStoreName='北京仓库') | Q(orderStoreName='北京分仓'))
        queryset_pos = None
        queryset_store = queryset_3.filter(Q(storeName='北京仓库') | Q(storeName='北京分仓'))

    elif channal == 'B2B' and region == '总部机构' and depot == '北京仓库':
        queryset_order = queryset_1.filter(orderStoreName='北京仓库')
        queryset_goods = queryset_4.filter(orderStoreName='北京仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='北京仓库')

    elif channal == 'B2B' and region == '总部机构' and depot == '北京分仓':
        queryset_order = queryset_1.filter(orderStoreName='北京分仓')
        queryset_goods = queryset_4.filter(orderStoreName='北京分仓')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='北京分仓')

    elif channal == 'B2B' and region == '华北大区' and depot == '天津仓库':
        queryset_order = queryset_1.filter(Q(orderStoreName='天津仓库'))
        queryset_goods = queryset_4.filter(Q(orderStoreName='天津仓库'))
        queryset_pos = None
        queryset_store = queryset_3.filter(Q(storeName='天津仓库'))

    elif channal == 'B2B' and region == '双鸭山分公司' and depot == '双鸭山仓库':
        queryset_order = queryset_1.filter(orderStoreName='双鸭山仓库')
        queryset_goods = queryset_4.filter(orderStoreName='双鸭山仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='双鸭山仓库')

    elif channal == 'B2B' and region == '东北大区' and depot == '沈阳仓库':
        queryset_order = queryset_1.filter(orderStoreName='沈阳仓库')
        queryset_goods = queryset_4.filter(orderStoreName='沈阳仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='沈阳仓库')

    elif channal == 'B2B' and region == '华南大区' and depot == '深圳仓库':
        queryset_order = queryset_1.filter(orderStoreName='深圳仓库')
        queryset_goods = queryset_4.filter(orderStoreName='深圳仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='深圳仓库')

    elif channal == 'B2B' and region == '西南大区' and depot == '成都仓库':
        queryset_order = queryset_1.filter(orderStoreName='成都仓库')
        queryset_goods = queryset_4.filter(orderStoreName='成都仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='成都仓库')

    elif channal == 'B2B' and region == '北方大区' and depot == '呼和浩特仓库':
        queryset_order = queryset_1.filter(orderStoreName='呼和浩特仓库')
        queryset_goods = queryset_4.filter(orderStoreName='呼和浩特仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='呼和浩特仓库')

    elif channal == 'B2B' and region == '华东大区' and depot == '上海仓库':
        queryset_order = queryset_1.filter(orderStoreName='上海仓库')
        queryset_goods = queryset_4.filter(orderStoreName='上海仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='上海仓库')

    elif channal == 'B2B' and region == '西北大区' and depot == '兰州仓库':
        queryset_order = queryset_1.filter(orderStoreName='兰州仓库')
        queryset_goods = queryset_4.filter(orderStoreName='兰州仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='兰州仓库')

    elif channal == 'B2B' and region == '中原大区' and depot == '郑州仓库':
        queryset_order = queryset_1.filter(orderStoreName='郑州仓库')
        queryset_goods = queryset_4.filter(orderStoreName='郑州仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='郑州仓库')



    elif channal == 'B2C' and region == '全部区域' and depot == '全部配送中心':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(Q(orderStoreName='禾中便利店0001') |
                                            Q(orderStoreName='北京分仓') |
                                            Q(orderStoreName='禾中便利店0002') |
                                            Q(orderStoreName='直营门店') |
                                            Q(orderStoreName='北京分仓门店') |
                                            Q(orderStoreName='北京仓库') |
                                            Q(orderStoreName='天津仓库') |
                                            Q(orderStoreName='天津分仓门店') |
                                            Q(orderStoreName='双鸭山仓库') |
                                            Q(orderStoreName='双鸭山分仓门店') |
                                            Q(orderStoreName='沈阳仓库') |
                                            Q(orderStoreName='沈阳分仓门店') |
                                            Q(orderStoreName='深圳仓库') |
                                            Q(orderStoreName='深圳分仓门店') |
                                            Q(orderStoreName='成都仓库') |
                                            Q(orderStoreName='呼和浩特仓库') |
                                            Q(orderStoreName='上海仓库') |
                                            Q(orderStoreName='兰州仓库') |
                                            Q(orderStoreName='郑州仓库'))
        queryset_store = queryset_3.filter(Q(storeName='禾中便利店0001') |
                                            Q(storeName='北京分仓') |
                                            Q(storeName='禾中便利店0002') |
                                            Q(storeName='直营门店') |
                                            Q(storeName='北京分仓门店') |
                                            Q(storeName='北京仓库') |
                                            Q(storeName='天津仓库') |
                                            Q(storeName='天津分仓门店') |
                                            Q(storeName='双鸭山仓库') |
                                            Q(storeName='双鸭山分仓门店') |
                                            Q(storeName='沈阳仓库') |
                                            Q(storeName='沈阳分仓门店') |
                                            Q(storeName='深圳仓库') |
                                            Q(storeName='深圳分仓门店') |
                                            Q(storeName='成都仓库') |
                                            Q(storeName='呼和浩特仓库') |
                                            Q(storeName='上海仓库') |
                                            Q(storeName='兰州仓库') |
                                            Q(storeName='郑州仓库'))

    elif channal == 'B2C' and region == '总部机构' and depot == '全部配送中心':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(Q(orderStoreName='禾中便利店0001') |
                                            Q(orderStoreName='北京分仓') |
                                            Q(orderStoreName='禾中便利店0002') |
                                            Q(orderStoreName='直营门店') |
                                            Q(orderStoreName='北京分仓门店') |
                                            Q(orderStoreName='北京仓库'))
        queryset_store = queryset_3.filter(Q(storeName='禾中便利店0001') |
                                            Q(storeName='北京分仓') |
                                            Q(storeName='禾中便利店0002') |
                                            Q(storeName='直营门店') |
                                            Q(storeName='北京分仓门店') |
                                            Q(storeName='北京仓库'))

    elif channal == 'B2C' and region == '总部机构' and depot == '禾中便利店0001':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='禾中便利店0001')
        queryset_store = queryset_3.filter(storeName='禾中便利店0001')
    elif channal == 'B2C' and region == '总部机构' and depot == '北京分仓':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='北京分仓')
        queryset_store = queryset_3.filter(storeName='北京分仓')

    elif channal == 'B2C' and region == '总部机构' and depot == '禾中便利店0002':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='禾中便利店0002')
        queryset_store = queryset_3.filter(storeName='禾中便利店0002')
    elif channal == 'B2C' and region == '总部机构' and depot == '直营门店':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='直营门店')
        queryset_store = queryset_3.filter(storeName='直营门店')
    elif channal == 'B2C' and region == '总部机构' and depot == '北京分仓门店':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='北京分仓门店')
        queryset_store = queryset_3.filter(storeName='北京分仓门店')
    elif channal == 'B2C' and region == '总部机构' and depot == '北京仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='北京仓库')
        queryset_store = queryset_3.filter(storeName='北京仓库')

    elif channal == 'B2C' and region == '华北大区' and depot == '全部配送中心':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(Q(orderStoreName='天津仓库') |
                                         Q(orderStoreName='天津分仓门店'))
        queryset_store = queryset_3.filter(Q(storeName='天津仓库') |
                                         Q(storeName='天津分仓门店'))
    elif channal == 'B2C' and region == '华北大区' and depot == '天津仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='天津仓库')
        queryset_store = queryset_3.filter(storeName='天津仓库')
    elif channal == 'B2C' and region == '华北大区' and depot == '天津分仓门店':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='天津分仓门店')
        queryset_store = queryset_3.filter(storeName='天津分仓门店')



    elif channal == 'B2C' and region == '双鸭山分公司' and depot == '全部配送中心':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(Q(orderStoreName='双鸭山仓库') |
                                         Q(orderStoreName='双鸭山分仓门店'))
        queryset_store = queryset_3.filter(Q(storeName='双鸭山仓库') |
                                         Q(storeName='双鸭山分仓门店'))

    elif channal == 'B2C' and region == '双鸭山分公司' and depot == '双鸭山仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='双鸭山仓库')
        queryset_store = queryset_3.filter(storeName='双鸭山仓库')
    elif channal == 'B2C' and region == '双鸭山分公司' and depot == '双鸭山分仓门店':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='双鸭山分仓门店')
        queryset_store = queryset_3.filter(storeName='双鸭山分仓门店')



    elif channal == 'B2C' and region == '东北大区' and depot == '全部配送中心':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(Q(orderStoreName='沈阳仓库') |
                                         Q(orderStoreName='沈阳分仓门店'))
        queryset_store = queryset_3.filter(Q(storeName='沈阳仓库') |
                                         Q(storeName='沈阳分仓门店'))

    elif channal == 'B2C' and region == '东北大区' and depot == '沈阳仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='沈阳仓库')
        queryset_store = queryset_3.filter(storeName='沈阳仓库')

    elif channal == 'B2C' and region == '东北大区' and depot == '沈阳分仓门店':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='沈阳分仓门店')
        queryset_store = queryset_3.filter(storeName='沈阳分仓门店')


    elif channal == 'B2C' and region == '华南大区' and depot == '全部配送中心':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(Q(orderStoreName='深圳仓库') |
                                         Q(orderStoreName='深圳分仓门店'))
        queryset_store = queryset_3.filter(Q(storeName='深圳仓库') |
                                         Q(storeName='深圳分仓门店'))
    elif channal == 'B2C' and region == '华南大区' and depot == '深圳仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='深圳仓库')
        queryset_store = queryset_3.filter(storeName='深圳仓库')

    elif channal == 'B2C' and region == '华南大区' and depot == '深圳分仓门店':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='深圳分仓门店')
        queryset_store = queryset_3.filter(storeName='深圳分仓门店')


    elif channal == 'B2C' and region == '西南大区' and depot == '成都仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='成都仓库')
        queryset_store = queryset_3.filter(storeName='成都仓库')
    elif channal == 'B2C' and region == '北方大区' and depot == '呼和浩特仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='呼和浩特仓库')
        queryset_store = queryset_3.filter(storeName='呼和浩特仓库')
    elif channal == 'B2C' and region == '华东大区' and depot == '上海仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='上海仓库')
        queryset_store = queryset_3.filter(storeName='上海仓库')
    elif channal == 'B2C' and region == '西北大区' and depot == '兰州仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='兰州仓库')
        queryset_store = queryset_3.filter(storeName='兰州仓库')
    elif channal == 'B2C' and region == '中原大区' and depot == '郑州仓库':
        queryset_order = None
        queryset_goods = None
        queryset_pos = queryset_2.filter(orderStoreName='郑州仓库')
        queryset_store = queryset_3.filter(storeName='郑州仓库')

    elif channal == '电商渠道' and region == '总部机构' and depot == '全部配送中心':
        queryset_order = queryset_1.filter(Q(orderStoreName='京东官方直营店') |
                                            Q(orderStoreName='京东九河泉仓库') |
                                            Q(orderStoreName='民生银行仓库'))
        queryset_goods = queryset_4.filter(Q(orderStoreName='京东官方直营店') |
                                           Q(orderStoreName='京东九河泉仓库') |
                                           Q(orderStoreName='民生银行仓库'))
        queryset_pos = None
        queryset_store = queryset_3.filter(Q(storeName='京东官方直营店') |
                                            Q(storeName='京东九河泉仓库') |
                                            Q(storeName='民生银行仓库'))

    elif channal == '电商渠道' and region == '总部机构' and depot == '京东官方直营店':
        queryset_order = queryset_1.filter(orderStoreName='京东官方直营店')
        queryset_goods = queryset_4.filter(orderStoreName='京东官方直营店')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='京东官方直营店')

    elif channal == '电商渠道' and region == '总部机构' and depot == '京东九河泉仓库':
        queryset_order = queryset_1.filter(orderStoreName='京东九河泉仓库')
        queryset_goods = queryset_4.filter(orderStoreName='京东九河泉仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='京东九河泉仓库')

    elif channal == '电商渠道' and region == '总部机构' and depot == '民生银行仓库':
        queryset_order = queryset_1.filter(orderStoreName='民生银行仓库')
        queryset_goods = queryset_4.filter(orderStoreName='民生银行仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='民生银行仓库')

    elif channal == '电视购物' and region == '总部机构' and depot == '电视购物仓库':
        queryset_order = queryset_1.filter(orderStoreName='电视购物仓库')
        queryset_goods = queryset_4.filter(orderStoreName='电视购物仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(storeName='电视购物仓库')

    elif channal == '禾中农业' and region == '总部机构' and depot == '全部配送中心':
        queryset_order = queryset_1.filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单'))
        queryset_goods = queryset_4.filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单'))
        queryset_pos = None
        queryset_store = queryset_3.filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单'))

    elif channal == '禾中农业' and region == '总部机构' and depot == '禾中农业仓库':
        queryset_order = queryset_1.filter(orderStoreName='禾中农业仓库')
        queryset_goods = queryset_4.filter(orderStoreName='禾中农业仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(orderStoreName='禾中农业仓库')

    elif channal == '禾中农业' and region == '总部机构' and depot == '农业订单':
        queryset_order = queryset_1.filter(orderStoreName='农业订单')
        queryset_goods = queryset_4.filter(orderStoreName='农业订单')
        queryset_pos = None
        queryset_store = queryset_3.filter(orderStoreName='农业订单')

    elif channal == '产品部' and region == '总部机构' and depot == '产品部仓库':
        queryset_order = queryset_1.filter(orderStoreName='产品部仓库')
        queryset_goods = queryset_4.filter(orderStoreName='产品部仓库')
        queryset_pos = None
        queryset_store = queryset_3.filter(orderStoreName='产品部仓库')


    order_orderamount = 0 if queryset_order == None else queryset_order.aggregate(Sum('amount'))['amount__sum']
    pos_orderamount = 0 if queryset_pos == None else queryset_pos.aggregate(Sum('amount'))['amount__sum']

    order_count= 0 if queryset_order == None else len(queryset_order.filter(amount__gt=0))
    pos_count = 0 if queryset_pos == None else len(queryset_pos.filter(amount__gt=0))

    order_cuscount = len(queryset_order.values('memberPin').distinct())
    # pos_cuscount = queryset_pos.values('memberPin').distinct()
    # print(order_cuscount)

    store_reg_count = len(queryset_store)

    # res['订单金额'] = int(order_orderamount + pos_orderamount)
    # res['订单数量'] = int(order_count + pos_count)
    # res['下单客户数'] = int(order_cuscount)
    # res['新增客户数'] = int(store_reg_count)

    res['part1'] = {'订单金额': int(order_orderamount + pos_orderamount),
                    '订单数量': int(order_count + pos_count),
                    '下单客户数': int(order_cuscount),
                    '新增客户数': int(store_reg_count),

            }


    b2b = queryset_1.filter(Q(orderStoreName='北京仓库') |
                            Q(orderStoreName='北京分仓') |
                            Q(orderStoreName='天津仓库') |
                            Q(orderStoreName='双鸭山仓库') |
                            Q(orderStoreName='沈阳仓库') |
                            Q(orderStoreName='深圳仓库') |
                            Q(orderStoreName='成都仓库') |
                            Q(orderStoreName='呼和浩特仓库') |
                            Q(orderStoreName='上海仓库') |
                            Q(orderStoreName='兰州仓库') |
                            Q(orderStoreName='郑州仓库')).aggregate(Sum('amount'))['amount__sum']


    b2c = queryset_2.filter(Q(orderStoreName='禾中便利店0001') |
                            Q(orderStoreName='北京分仓') |
                            Q(orderStoreName='禾中便利店0002') |
                            Q(orderStoreName='直营门店') |
                            Q(orderStoreName='北京分仓门店') |
                            Q(orderStoreName='北京仓库') |
                            Q(orderStoreName='天津仓库') |
                            Q(orderStoreName='天津分仓门店') |
                            Q(orderStoreName='双鸭山仓库') |
                            Q(orderStoreName='双鸭山分仓门店') |
                            Q(orderStoreName='沈阳仓库') |
                            Q(orderStoreName='沈阳分仓门店') |
                            Q(orderStoreName='深圳仓库') |
                            Q(orderStoreName='深圳分仓门店') |
                            Q(orderStoreName='成都仓库') |
                            Q(orderStoreName='呼和浩特仓库') |
                            Q(orderStoreName='上海仓库') |
                            Q(orderStoreName='兰州仓库') |
                            Q(orderStoreName='郑州仓库')).aggregate(Sum('amount'))['amount__sum']

    agriculture =queryset_1.filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单')).aggregate(Sum('amount'))[
        'amount__sum']  # 农业
    online = queryset_1.filter(Q(orderStoreName='京东九河泉仓库') | Q(orderStoreName='京东官方直营店') | Q(orderStoreName='民生银行仓库')).aggregate(
        Sum('amount'))['amount__sum']  # 电商
    television = queryset_1.filter(orderStoreName='电视购物仓库').aggregate(Sum('amount'))['amount__sum']  # 电视
    # taste = queryset_list_month[0].filter(orderStoreName='禾中味道官方直营店').aggregate(Sum('amount'))['amount__sum']# 禾中味道
    direct_store = queryset_1.filter(orderStoreName='直营门店').aggregate(Sum('amount'))['amount__sum']  # 直营店
    chanpinbu = queryset_1.filter(orderStoreName='产品部仓库').aggregate(Sum('amount'))['amount__sum']

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
    if b2b == None:
        b2b = 0
    if direct_store == None:
        direct_store = 0

    # res['B2B'] = int(b2b)
    # res['B2C'] = int(b2c)
    # res['禾中农业'] = int(agriculture)
    # res['电商渠道'] = int(online)
    # res['电视购物'] = int(television)
    # res['产品部'] = int(chanpinbu)

    res['part2'] = {
        'B2B': int(b2b),
        'B2C': int(b2c),
        '禾中农业': int(agriculture),
        '电商渠道': int(online),
        '电视购物': int(television),
        '产品部': int(chanpinbu)
    }
    try:
        time_seconds = make_time(ryear, rmonth, rday+1) - make_time(lyear, lmonth, lday)

    except:
        try:
            time_seconds = make_time(ryear, rmonth+1, 1) - make_time(lyear, lmonth, lday)
        except:
            time_seconds = make_time(ryear+1, 1, 1) - make_time(lyear, lmonth, lday)

    time_days = time_seconds / 60 / 60 / 24
    # print(queryset_order.extra(select={'month': 'extract( month from createDate )'}).values('month').annotate(sum=Sum('amount')))

    # order_orderamount = 0 if queryset_order == None else queryset_order.aggregate(Sum('amount'))['amount__sum']
    # pos_orderamount = 0 if queryset_pos == None else queryset_pos.aggregate(Sum('amount'))['amount__sum']
    if time_days < 3:
        # 趋势按照小时返回
        try:
            data_list_order = list(queryset_order.extra(select={"hour": """DATE_FORMAT( createDate,'%%Y-%%m-%%d %%H')"""}).values('hour').annotate(sum=Sum('amount')))
        except:
            data_list_order = []
        try:
            data_list_pos = list(queryset_pos.extra(select={"hour": """DATE_FORMAT(createDate,'%%Y-%%m-%%d %%H')"""}).values('hour').annotate(sum=Sum('amount')))
        except:
            data_list_pos = []

        tmp_foo = 'hour'

    elif 3 <= time_days < 32:
        # 趋势按照天返回
        try:
            data_list_order = list(queryset_order.extra(select={'day': """DATE_FORMAT(createDate,'%%Y-%%m-%%d')"""}).values('day').annotate(sum=Sum('amount')))
        except:
            data_list_order = []
        try:
            data_list_pos = list(queryset_pos.extra(select={'day': """DATE_FORMAT(createDate,'%%Y-%%m-%%d')"""}).values('day').annotate(sum=Sum('amount')))
        except:
            data_list_pos = []
        tmp_foo = 'day'

    elif 32 <= time_days < 100:
        # 趋势按照周返回
        try:
            data_list_order = list(queryset_order.extra(select={'week': 'extract( week from createDate )'}).values('week').annotate(sum=Sum('amount')))
        except:
            data_list_order = []
        try:
            data_list_pos = list(queryset_pos.extra(select={'week': 'extract( week from createDate )'}).values('week').annotate(sum=Sum('amount')))
        except:
            data_list_pos = []
        tmp_foo = 'week'

    elif time_days >= 100:
        try:
            data_list_order = list(queryset_order.extra(select={'month': """DATE_FORMAT( createDate,'%%Y-%%m')"""}).values('month').annotate(sum=Sum('amount')))
        except:
            data_list_order = []
        try:
            data_list_pos = list(queryset_pos.extra(select={'month': """DATE_FORMAT( createDate,'%%Y-%%m')"""}).values('month').annotate(sum=Sum('amount')))
        except:
            data_list_pos = []
        tmp_foo = 'month'

    dt1 = {}
    if len(data_list_order) > 0:
        for i in data_list_order:
            dt1[i[tmp_foo]] = round(i['sum'],2)
    dt2 = {}
    if len(data_list_pos) > 0:
        for i in data_list_pos:
            dt2[i[tmp_foo]] = round(i['sum'],2)
    X, Y = Counter(dt1), Counter(dt2)
    dict_foo = dict(X+Y)

    dict_bar = {}

    if tmp_foo == 'hour':
        starttime = str(lyear)+'-'+str(lmonth)+'-'+str(lday)+' 0'
        endtime =str(ryear)+'-'+str(rmonth)+'-'+str(rday)+' 23'
        hour_list = getEveryHour(starttime, endtime)
        for i in hour_list:
            if i in dict_foo.keys():
                dict_bar[i] = dict_foo[i]
            else:
                dict_bar[i] = 0
    elif tmp_foo == 'day':
        starttime = str(lyear) + '-' + str(lmonth) + '-' + str(lday)
        endtime = str(ryear) + '-' + str(rmonth) + '-' + str(rday)
        day_list = getEveryDay(starttime, endtime)
        for i in day_list:
            if i in dict_foo.keys():
                dict_bar[i] = dict_foo[i]
            else:
                dict_bar[i] = 0


    dataresult = []
    if dict_bar == {}:
        for i in dict_foo:
            dataresult.append({i: dict_foo[i]})
        res['part3'] = {'销售趋势': dataresult, '类型': tmp_foo}
        # res['销售趋势'] = dict_foo
    else:
        for i in dict_bar:
            dataresult.append({i: dict_bar[i]})
        res['part3'] = {'销售趋势': dataresult, '类型': tmp_foo}
        # res['销售趋势'] = dict_bar

    try:
        classify_data_goods = list(queryset_goods.values('secondIcatName').annotate(Sum('amount')))
    except:
        classify_data_goods = []

    try:
        classify_data_pos = list(queryset_pos.values('secondIcatName').annotate(Sum('amount')))
    except:
        classify_data_pos = []

    data_dict_goods = {}
    for i in classify_data_goods:
        data_dict_goods[i['secondIcatName']] = int(i['amount__sum'])

    data_dict_pos = {}
    for i in  classify_data_pos:
        data_dict_pos[i['secondIcatName']] = int(i['amount__sum'])

    U, V = Counter(data_dict_goods), Counter(data_dict_pos)

    res['part4'] = {'商品分类销售额': dict(U + V)}

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

        channal = request.GET.get('channal', '全部渠道')
        region = request.GET.get('region', '全部区域')
        depot = request.GET.get('depot', '全部配送中心')

        queryset_2 = b2b_posgoods.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
                                                               createDate__lte=datetime(ryear, rmonth, rday, 23, 59,
                                                                                        59))
        queryset_4 = b2b_goodstable.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
                                                                 createDate__lte=datetime(ryear, rmonth, rday, 23, 59,
                                                                                          59))

        if channal == '全部渠道' and region == '全部区域' and depot == '全部配送中心':
            queryset_pos = queryset_2
            queryset_goods = queryset_4

        elif channal == 'B2B' and region == '全部区域' and depot == '全部配送中心':
            queryset_goods = queryset_4.filter(Q(orderStoreName='北京仓库') |
                                               Q(orderStoreName='北京分仓') |
                                               Q(orderStoreName='天津仓库') |
                                               Q(orderStoreName='双鸭山仓库') |
                                               Q(orderStoreName='沈阳仓库') |
                                               Q(orderStoreName='深圳仓库') |
                                               Q(orderStoreName='成都仓库') |
                                               Q(orderStoreName='呼和浩特仓库') |
                                               Q(orderStoreName='上海仓库') |
                                               Q(orderStoreName='兰州仓库') |
                                               Q(orderStoreName='郑州仓库'))

            queryset_pos = None

        elif channal == 'B2B' and region == '总部机构' and depot == '全部配送中心':
            queryset_goods = queryset_4.filter(Q(orderStoreName='北京仓库') | Q(orderStoreName='北京分仓'))
            queryset_pos = None

        elif channal == 'B2B' and region == '总部机构' and depot == '北京仓库':
            queryset_goods = queryset_4.filter(orderStoreName='北京仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '总部机构' and depot == '北京分仓':
            queryset_goods = queryset_4.filter(orderStoreName='北京分仓')
            queryset_pos = None

        elif channal == 'B2B' and region == '华北大区' and depot == '天津仓库':
            queryset_goods = queryset_4.filter(Q(orderStoreName='天津仓库'))
            queryset_pos = None

        elif channal == 'B2B' and region == '双鸭山分公司' and depot == '双鸭山仓库':
            queryset_goods = queryset_4.filter(orderStoreName='双鸭山仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '东北大区' and depot == '沈阳仓库':
            queryset_goods = queryset_4.filter(orderStoreName='沈阳仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '华南大区' and depot == '深圳仓库':
            queryset_goods = queryset_4.filter(orderStoreName='深圳仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '西南大区' and depot == '成都仓库':
            queryset_goods = queryset_4.filter(orderStoreName='成都仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '北方大区' and depot == '呼和浩特仓库':
            queryset_goods = queryset_4.filter(orderStoreName='呼和浩特仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '华东大区' and depot == '上海仓库':
            queryset_goods = queryset_4.filter(orderStoreName='上海仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '西北大区' and depot == '兰州仓库':
            queryset_goods = queryset_4.filter(orderStoreName='兰州仓库')
            queryset_pos = None

        elif channal == 'B2B' and region == '中原大区' and depot == '郑州仓库':
            queryset_goods = queryset_4.filter(orderStoreName='郑州仓库')
            queryset_pos = None


        elif channal == 'B2C' and region == '全部区域' and depot == '全部配送中心':
            queryset_goods = None
            queryset_pos = queryset_2.filter(Q(orderStoreName='禾中便利店0001') |
                                             Q(orderStoreName='北京分仓') |
                                             Q(orderStoreName='禾中便利店0002') |
                                             Q(orderStoreName='直营门店') |
                                             Q(orderStoreName='北京分仓门店') |
                                             Q(orderStoreName='北京仓库') |
                                             Q(orderStoreName='天津仓库') |
                                             Q(orderStoreName='天津分仓门店') |
                                             Q(orderStoreName='双鸭山仓库') |
                                             Q(orderStoreName='双鸭山分仓门店') |
                                             Q(orderStoreName='沈阳仓库') |
                                             Q(orderStoreName='沈阳分仓门店') |
                                             Q(orderStoreName='深圳仓库') |
                                             Q(orderStoreName='深圳分仓门店') |
                                             Q(orderStoreName='成都仓库') |
                                             Q(orderStoreName='呼和浩特仓库') |
                                             Q(orderStoreName='上海仓库') |
                                             Q(orderStoreName='兰州仓库') |
                                             Q(orderStoreName='郑州仓库'))

        elif channal == 'B2C' and region == '总部机构' and depot == '全部配送中心':
            queryset_goods = None
            queryset_pos = queryset_2.filter(Q(orderStoreName='禾中便利店0001') |
                                             Q(orderStoreName='北京分仓') |
                                             Q(orderStoreName='禾中便利店0002') |
                                             Q(orderStoreName='直营门店') |
                                             Q(orderStoreName='北京分仓门店') |
                                             Q(orderStoreName='北京仓库'))

        elif channal == 'B2C' and region == '总部机构' and depot == '禾中便利店0001':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='禾中便利店0001')
        elif channal == 'B2C' and region == '总部机构' and depot == '北京分仓':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='北京分仓')

        elif channal == 'B2C' and region == '总部机构' and depot == '禾中便利店0002':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='禾中便利店0002')
        elif channal == 'B2C' and region == '总部机构' and depot == '直营门店':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='直营门店')
        elif channal == 'B2C' and region == '总部机构' and depot == '北京分仓门店':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='北京分仓门店')
        elif channal == 'B2C' and region == '总部机构' and depot == '北京仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='北京仓库')

        elif channal == 'B2C' and region == '华北大区' and depot == '全部配送中心':
            queryset_goods = None
            queryset_pos = queryset_2.filter(Q(orderStoreName='天津仓库') |
                                             Q(orderStoreName='天津分仓门店'))

        elif channal == 'B2C' and region == '华北大区' and depot == '天津仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='天津仓库')

        elif channal == 'B2C' and region == '华北大区' and depot == '天津分仓门店':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='天津分仓门店')



        elif channal == 'B2C' and region == '双鸭山分公司' and depot == '全部配送中心':
            queryset_goods = None
            queryset_pos = queryset_2.filter(Q(orderStoreName='双鸭山仓库') |
                                             Q(orderStoreName='双鸭山分仓门店'))


        elif channal == 'B2C' and region == '双鸭山分公司' and depot == '双鸭山仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='双鸭山仓库')

        elif channal == 'B2C' and region == '双鸭山分公司' and depot == '双鸭山分仓门店':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='双鸭山分仓门店')


        elif channal == 'B2C' and region == '东北大区' and depot == '全部配送中心':
            queryset_goods = None
            queryset_pos = queryset_2.filter(Q(orderStoreName='沈阳仓库') |
                                             Q(orderStoreName='沈阳分仓门店'))


        elif channal == 'B2C' and region == '东北大区' and depot == '沈阳仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='沈阳仓库')

        elif channal == 'B2C' and region == '东北大区' and depot == '沈阳分仓门店':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='沈阳分仓门店')


        elif channal == 'B2C' and region == '华南大区' and depot == '全部配送中心':
            queryset_goods = None
            queryset_pos = queryset_2.filter(Q(orderStoreName='深圳仓库') |
                                             Q(orderStoreName='深圳分仓门店'))
        elif channal == 'B2C' and region == '华南大区' and depot == '深圳仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='深圳仓库')


        elif channal == 'B2C' and region == '华南大区' and depot == '深圳分仓门店':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='深圳分仓门店')

        elif channal == 'B2C' and region == '西南大区' and depot == '成都仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='成都仓库')
        elif channal == 'B2C' and region == '北方大区' and depot == '呼和浩特仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='呼和浩特仓库')

        elif channal == 'B2C' and region == '华东大区' and depot == '上海仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='上海仓库')

        elif channal == 'B2C' and region == '西北大区' and depot == '兰州仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='兰州仓库')

        elif channal == 'B2C' and region == '中原大区' and depot == '郑州仓库':
            queryset_goods = None
            queryset_pos = queryset_2.filter(orderStoreName='郑州仓库')


        elif channal == '电商渠道' and region == '总部机构' and depot == '全部配送中心':
            queryset_goods = queryset_4.filter(Q(orderStoreName='京东官方直营店') |
                                               Q(orderStoreName='京东九河泉仓库') |
                                               Q(orderStoreName='民生银行仓库'))
            queryset_pos = None


        elif channal == '电商渠道' and region == '总部机构' and depot == '京东官方直营店':
            queryset_goods = queryset_4.filter(orderStoreName='京东官方直营店')
            queryset_pos = None


        elif channal == '电商渠道' and region == '总部机构' and depot == '京东九河泉仓库':
            queryset_goods = queryset_4.filter(orderStoreName='京东九河泉仓库')
            queryset_pos = None


        elif channal == '电商渠道' and region == '总部机构' and depot == '民生银行仓库':
            queryset_goods = queryset_4.filter(orderStoreName='民生银行仓库')
            queryset_pos = None

        elif channal == '电视购物' and region == '总部机构' and depot == '电视购物仓库':
            queryset_goods = queryset_4.filter(orderStoreName='电视购物仓库')
            queryset_pos = None


        elif channal == '禾中农业' and region == '总部机构' and depot == '全部配送中心':
            queryset_goods = queryset_4.filter(Q(orderStoreName='禾中农业仓库') | Q(orderStoreName='农业订单'))
            queryset_pos = None

        elif channal == '禾中农业' and region == '总部机构' and depot == '禾中农业仓库':
            queryset_goods = queryset_4.filter(orderStoreName='禾中农业仓库')
            queryset_pos = None

        elif channal == '禾中农业' and region == '总部机构' and depot == '农业订单':
            queryset_goods = queryset_4.filter(orderStoreName='农业订单')
            queryset_pos = None

        elif channal == '产品部' and region == '总部机构' and depot == '产品部仓库':
            queryset_goods = queryset_4.filter(orderStoreName='产品部仓库')
            queryset_pos = None


        queryset_pos1 =  queryset_pos.filter(secondIcatName=classify)
        queryset_goodstb = queryset_goods.filter(secondIcatName=classify)


        data_pos = queryset_pos1.values('skuName').annotate(Sum('amount'))

        data_goodstb = queryset_goodstb.values('skuName').annotate(Sum('amount'))

        # count_pos = queryset_pos.aggregate(Sum('skuNum'))
        # count_goodstb = queryset_goodstb.aggregate(Sum('skuNum'))
        # print(count_pos)

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
        # print(recvs)
        sums = 0
        for i in recvs.values():
            sums = sums + i
        # print(sums)
        recv = {}
        for i in range(len(ret)):
            recv[ret[i][0]] = ret[i][1]
        # print(recv)

        sum = 0
        for i in recv.values():
            sum = sum + i
        # print(sum)
        recvs['其它'] = int(sum) - int(sums)
        res['amount'] = int(sum)
        res['data'] = recvs
        # res['count'] = int(count_pos['skuNum__sum'])+int(count_goodstb['skuNum__sum'])

        return JsonResponse(res)


# 请求 获取复选框内容
def basecheck(request):

    pass

####
#
# {
#     '全部渠道':{'全部区域':{'全部配送中心',},},
#     'B2B':{'总部机构':{'全部配送中心',
#                    '北京仓库',
#                    '北京分仓'},
#             '华北大区':{'天津仓库',},
#             '双鸭山分公司':{'双鸭山仓库',},
#             '东北大区':{'沈阳仓库',},
#             '华南大区':{'深圳仓库',},
#             '西南大区':{'成都仓库',},
#             '北方大区':{'呼和浩特仓库',},
#             '华东大区':{'上海仓库',},
#             '西北大区':{'兰州仓库',},
#             '中原大区':{'郑州仓库',},
#             '全部区域':{'全部配送中心',},
#            },
#     'B2C':{'总部机构':{'全部配送中心',
#                    '禾中便利店0001',
#                    '禾中便利店0002',
#                    '北京分仓',
#                    '北京仓库',
#                    '北京分仓门店',
#                    '直营门店',},
#             '华北大区':{'全部配送中心',
#                     '天津仓库',
#                     '天津分仓门店',},
#             '双鸭山分公司':{'全部配送中心',
#                       '双鸭山仓库',
#                       '双鸭山分仓门店',},
#             '东北大区':{'全部配送中心',
#                     '沈阳仓库',
#                     '沈阳分仓门店',},
#             '华南大区':{'全部配送中心',
#                     '深圳仓库',
#                     '深圳分仓门店',},
#             '西南大区':{'成都仓库',},
#             '北方大区':{'呼和浩特仓库',},
#             '华东大区':{'上海仓库',},
#             '西北大区':{'兰州仓库',},
#             '中原大区':{'郑州仓库',},
#             '全部区域':{'全部配送中心',},
#            },
#     '电商渠道':{'总部机构':['全部配送中心',
#                     '京东官方直营店',
#                     '京东九河泉仓库',
#                     '民生银行仓库',},},
#     '电视购物':{'总部机构':['电视购物仓库',},},
#     '禾中农业':{'总部机构':['全部配送中心',
#                     '禾中农业仓库',
#                     '农业订单',},},
#     '产品部':{'总部机构':['产品部仓库',},},
#
# }
#
####
# def testing(request):
#     res = {}
#
#     incometd = incomeDay()
#     date_list = incometd._get_today()
#
#     channal = request.get('channal', None)
#     region = request.get('region', None)
#     depot = request.get('depot', None)
#
#     lyear = int(request.GET.get('lyear', date_list[0]))
#     lmonth = int(request.GET.get('lmonth', date_list[1]))
#     lday = int(request.GET.get('lday', '1'))
#     ryear = int(request.GET.get('ryear', date_list[0]))
#     rmonth = int(request.GET.get('rmonth', date_list[1]))
#     rday = int(request.GET.get('rday', date_list[2]))
#
#     queryset_order = b2b_ordertable.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
#                                                                   createDate__lte=datetime(ryear, rmonth, rday))
#     queryset_pos = b2b_posgoods.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
#                                                                  createDate__lte=datetime(ryear, rmonth, rday))
#
#     choice_channal = {
#         '全部渠道': [queryset_order,queryset_pos, ],
#         'B2B': [queryset_order.filter(Q(orderStoreName='北京仓库') |
#                                       Q(orderStoreName='北京分仓') |
#                                       Q(orderStoreName='天津仓库') |
#                                       Q(orderStoreName='双鸭山仓库') |
#                                       Q(orderStoreName='沈阳仓库') |
#                                       Q(orderStoreName='深圳仓库') |
#                                       Q(orderStoreName='成都仓库') |
#                                       Q(orderStoreName='呼和浩特仓库') |
#                                       Q(orderStoreName='上海仓库') |
#                                       Q(orderStoreName='兰州仓库') |
#                                       Q(orderStoreName='郑州仓库')), ],
#         'B2C': [queryset_pos, ],
#         '电商渠道': [queryset_order.filter(Q(orderStoreName='京东官方直营店') |
#                                        Q(orderStoreName='京东九河泉仓库') |
#                                        Q(orderStoreName='民生银行仓库')), ],
#
#         '电视购物': [queryset_order.filter(orderStoreName='电视购物仓库'), ],
#         '禾中农业': [queryset_order.filter(Q(orderStoreName='禾中农业仓库') |
#                                        Q(orderStoreName='农业订单')),],
#         '产品部': [queryset_order.filter(orderStoreName='产品部仓库'),],
#     }
#
#
#     if channal == 'B2B':
#         queryset_list_c = choice_channal['B2B']
#         choice_region = {
#             '总部机构': [queryset_list_c[0].filter(Q(orderStoreName='北京仓库') | Q(orderStoreName='北京分仓')),],
#             '华北大区': [queryset_list_c[0].filter(orderStoreName='天津仓库'),],
#             '双鸭山分公司': [queryset_list_c[0].filter(orderStoreName='双鸭山仓库'),],
#             '东北大区': [queryset_list_c[0].filter(orderStoreName='沈阳仓库'),],
#             '华南大区': [queryset_list_c[0].filter(orderStoreName='深圳仓库'),],
#             '西南大区': [queryset_list_c[0].filter(orderStoreName='成都仓库'),],
#             '北方大区': [queryset_list_c[0].filter(orderStoreName='呼和浩特仓库'),],
#             '华东大区': [queryset_list_c[0].filter(orderStoreName='上海仓库'),],
#             '西北大区': [queryset_list_c[0].filter(orderStoreName='兰州仓库'),],
#             '中原大区': [queryset_list_c[0].filter(orderStoreName='郑州仓库'),],
#             '全部大区': [queryset_list_c[0],],
#         }
#         if region == '总部机构':
#             queryset_list_r = choice_channal['总部机构']
#             depot_choice = {
#                 '北京仓库': [queryset_list_r[0].filter(orderStoreName='北京仓库'),],
#                 '北京分仓': [queryset_list_r[0].filter(orderStoreName='北京分仓')],
#                 '全部配送中心': [queryset_list_r[0],],
#             }
#             if depot == '北京仓库':
#                 queryset_list_end = depot_choice['北京仓库']
#             elif depot == '北京分仓':
#                 queryset_list_end = depot_choice['北京分仓']
#             elif depot == '全部配送中心':
#                 queryset_list_end = depot_choice['全部配送中心']
#
#         elif region == '华北大区':
#             queryset_list_r = choice_channal['华北大区']
#             depot_choice = {
#                 '天津仓库': [queryset_list_r[0],],
#             }
#             if depot == '天津仓库':
#                 queryset_list_end = depot_choice['天津仓库']
#
#         elif region == '双鸭山分公司':
#             queryset_list_r = choice_channal['双鸭山分公司']
#             depot_choice = {
#                 '双鸭山仓库': [queryset_list_r[0].filter(orderStoreName='双鸭山仓库'), ],
#             }
#             if depot == '双鸭山仓库':
#                 queryset_list_end = depot_choice['双鸭山仓库']
#         elif region == '东北大区':
#             queryset_list_r = choice_channal['东北大区']
#             depot_choice = {
#                 '沈阳仓库': [queryset_list_r[0].filter(orderStoreName='沈阳仓库'), ],
#             }
#             if depot == '沈阳仓库':
#                 queryset_list_end = depot_choice['沈阳仓库']
#         elif region == '华南大区':
#             queryset_list_r = choice_channal['华南大区']
#             depot_choice = {
#                 '深圳仓库': [queryset_list_r[0].filter(orderStoreName='深圳仓库'), ],
#             }
#             if depot == '深圳仓库':
#                 queryset_list_end = depot_choice['深圳仓库']
#         elif region == '西南大区':
#             queryset_list_r = choice_channal['西南大区']
#             depot_choice = {
#                 '成都仓库': [queryset_list_r[0].filter(orderStoreName='成都仓库'), ],
#             }
#             if depot == '成都仓库':
#                 queryset_list_end = depot_choice['成都仓库']
#         elif region == '北方大区':
#             queryset_list_r = choice_channal['北方大区']
#             depot_choice = {
#                 '呼和浩特仓库': [queryset_list_r[0].filter(orderStoreName='呼和浩特仓库'), ],
#             }
#             if depot == '呼和浩特仓库':
#                 queryset_list_end = depot_choice['呼和浩特仓库']
#         elif region == '华东大区':
#             queryset_list_r = choice_channal['华东大区']
#             depot_choice = {
#                 '上海仓库': [queryset_list_r[0].filter(orderStoreName='上海仓库'), ],
#             }
#             if depot == '上海仓库':
#                 queryset_list_end = depot_choice['上海仓库']
#         elif region == '西北大区':
#             queryset_list_r = choice_channal['西北大区']
#             depot_choice = {
#                 '兰州仓库': [queryset_list_r[0].filter(orderStoreName='兰州仓库'), ],
#             }
#             if depot == '兰州仓库':
#                 queryset_list_end = depot_choice['兰州仓库']
#         elif region == '中原大区':
#             queryset_list_r = choice_channal['中原大区']
#             depot_choice = {
#                 '郑州仓库': [queryset_list_r[0].filter(orderStoreName='郑州仓库'), ],
#             }
#             if depot == '郑州仓库':
#                 queryset_list_end = depot_choice['郑州仓库']
#         elif region == '全部大区':
#             queryset_list_end = choice_channal['全部大区']
#
#         elif region == '华北大区':
#             queryset_list = choice_channal['华北大区']
#         elif region == '双鸭山分公司':
#             queryset_list = choice_channal['双鸭山分公司']
#         elif region == '东北大区':
#             queryset_list = choice_channal['东北大区']
#         elif region == '华南大区':
#             queryset_list = choice_channal['华南大区']
#         elif region == '西南大区':
#             queryset_list = choice_channal['西南大区']
#         elif region == '北方大区':
#             queryset_list = choice_channal['北方大区']
#         elif region == '华东大区':
#             queryset_list = choice_channal['华东大区']
#         elif region == '西北大区':
#             queryset_list = choice_channal['西北大区']
#         elif region == '中原大区':
#             queryset_list = choice_channal['中原大区']
#         elif region == '全部配送中心':
#             queryset_list = choice_channal['西北大区']
#
#     elif channal == 'B2C':
#         queryset_list_c = choice_channal['B2C']
#         # choice_region = {
#         #     '总部机构': [queryset_list_c[0].filter(Q(orderStoreName='禾中便利店0001') | Q(orderStoreName='禾中便利店0002') | Q(orderStoreName='北京分仓') | Q(orderStoreName='直营门店') | Q(orderStoreName='北京分仓门店') | Q(orderStoreName='北京仓库')), ],
#         #     '华北大区': [queryset_list_c[0].filter(Q(orderStoreName='天津仓库') | Q(orderStoreName='天津分仓门店')), ],
#         #     '双鸭山分公司': [queryset_list_c[0].filter(Q(orderStoreName='双鸭山仓库') | Q(orderStoreName='双鸭山分仓门店')), ],
#         #     '东北大区': [queryset_list_c[0].filter(Q(orderStoreName='沈阳仓库') | Q(orderStoreName='沈阳分仓门店')),],
#         #     '华南大区': [queryset_list_c[0].filter(Q(orderStoreName='深圳仓库') | Q(orderStoreName='深圳分仓门店')),],
#         #     '西南大区': [queryset_list_c[0].filter(orderStoreName='成都仓库'),],
#         #     '北方大区': [queryset_list_c[0].filter(orderStoreName='呼和浩特仓库'), ],
#         #     '华东大区': [queryset_list_c[0].filter(orderStoreName='上海仓库'), ],
#         #     '西北大区': [queryset_list_c[0].filter(orderStoreName='兰州仓库'), ],
#         #     '中原大区': [queryset_list_c[0].filter(orderStoreName='郑州仓库'), ],
#         #     '全部大区': [queryset_list_c[0], ],
#         # }
#         if region == '总部机构':
#             if depot == '禾中便利店0001':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='禾中便利店0001')]
#             elif depot == '禾中便利店0002':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='禾中便利店0002')]
#             elif depot == '北京分仓':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='北京分仓')]
#             elif depot == '直营门店':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='直营门店')]
#             elif depot == '北京分仓门店':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='北京分仓门店')]
#             elif depot == '北京仓库':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='北京仓库')]
#             else:
#                 queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='禾中便利店0001') | Q(orderStoreName='禾中便利店0002') | Q(orderStoreName='北京分仓') | Q(orderStoreName='直营门店') | Q(orderStoreName='北京分仓门店') | Q(orderStoreName='北京仓库'))]
#         elif region == '华北大区':
#             if depot == '天津仓库':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='天津仓库')]
#             elif depot == '天津分仓门店':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='天津分仓门店')]
#             else:
#                 queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='天津仓库') | Q(orderStoreName='天津分仓门店')), ]
#         elif region == '双鸭山分公司':
#             if depot == '双鸭山仓库':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='双鸭山仓库')]
#             elif depot == '双鸭山分仓门店':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='双鸭山分仓门店')]
#             else:
#                 queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='双鸭山仓库') | Q(orderStoreName='双鸭山分仓门店')), ]
#         elif region == '东北大区':
#             if depot == '沈阳仓库':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='沈阳仓库')]
#             elif depot == '沈阳分仓门店':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='沈阳分仓门店')]
#             else:
#                 queryset_list_end = [
#                     queryset_list_c[0].filter(Q(orderStoreName='沈阳仓库') | Q(orderStoreName='沈阳分仓门店')), ]
#
#         elif region == '华南大区':
#             if depot == '深圳仓库':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='深圳仓库')]
#             elif depot == '深圳分仓门店':
#                 queryset_list_end = [queryset_list_c[0].filter(orderStoreName='深圳分仓门店')]
#             else:
#                 queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='深圳仓库') | Q(orderStoreName='深圳分仓门店')), ]
#         elif region == '西南大区':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='成都仓库'),]
#         elif region == '北方大区':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='呼和浩特仓库'), ]
#         elif region == '华东大区':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='成都仓库'), ]
#         elif region == '西北大区':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='兰州仓库'), ]
#         elif region == '中原大区':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='郑州仓库'), ]
#         elif region == '全部大区':
#             queryset_list_end = queryset_list_c
#
#
#     elif channal == '电商渠道':
#         queryset_list_c = choice_channal['电商渠道']
#         if depot == '京东官方直营店':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='京东官方直营店')]
#         elif depot == '京东九河泉仓库':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='京东九河泉仓库')]
#         elif depot == '民生银行仓库':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='民生银行仓库')]
#         else:
#             queryset_list_end = queryset_list_c
#
#     elif channal == '电视购物':
#         queryset_list_end = choice_channal['电视购物']
#
#     elif channal == '禾中农业':
#         queryset_list_c = choice_channal['禾中农业']
#         if depot == '禾中农业仓库':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='禾中农业仓库')]
#         elif depot == '农业订单':
#             queryset_list_end = [queryset_list_c[0].filter(orderStoreName='农业订单')]
#         else:
#             queryset_list_end = queryset_list_c
#
#     elif channal == '产品部':
#         queryset_list_end = choice_channal['产品部']
#     else:
#         queryset_list_end = choice_channal['全部渠道']
#
#     if len(queryset_list_end) == 1:
#         query = queryset_list_end[0]
#         order_amount = query.aggregate(Sum('amount'))['amount__sum']
#
#     elif len(queryset_list_end) == 2:
#         query1 = queryset_list_end[0]
#         query2 = queryset_list_end[1]
#
#     pass



