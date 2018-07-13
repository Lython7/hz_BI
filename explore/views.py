from datetime import datetime

from django.db.models import Q, Sum
from django.shortcuts import render
from hzyg.models import *


# Create your views here.
from overview.assistant import incomeDay


def explore(request):
    return render(request, 'explore/explore.html', context={})


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
def testing(request):
    res = {}

    incometd = incomeDay()
    date_list = incometd._get_today()

    channal = request.get('channal', None)
    region = request.get('region', None)
    depot = request.get('depot', None)

    lyear = int(request.GET.get('lyear', date_list[0]))
    lmonth = int(request.GET.get('lmonth', date_list[1]))
    lday = int(request.GET.get('lday', '1'))
    ryear = int(request.GET.get('ryear', date_list[0]))
    rmonth = int(request.GET.get('rmonth', date_list[1]))
    rday = int(request.GET.get('rday', date_list[2]))

    queryset_order = b2b_ordertable.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
                                                                  createDate__lte=datetime(ryear, rmonth, rday))
    queryset_pos = b2b_posgoods.objects.using('hzyg').filter(createDate__gte=datetime(lyear, lmonth, lday),
                                                                 createDate__lte=datetime(ryear, rmonth, rday))

    choice_channal = {
        '全部渠道': [queryset_order,queryset_pos, ],
        'B2B': [queryset_order.filter(Q(orderStoreName='北京仓库') |
                                      Q(orderStoreName='北京分仓') |
                                      Q(orderStoreName='天津仓库') |
                                      Q(orderStoreName='双鸭山仓库') |
                                      Q(orderStoreName='沈阳仓库') |
                                      Q(orderStoreName='深圳仓库') |
                                      Q(orderStoreName='成都仓库') |
                                      Q(orderStoreName='呼和浩特仓库') |
                                      Q(orderStoreName='上海仓库') |
                                      Q(orderStoreName='兰州仓库') |
                                      Q(orderStoreName='郑州仓库')), ],
        'B2C': [queryset_pos, ],
        '电商渠道': [queryset_order.filter(Q(orderStoreName='京东官方直营店') |
                                       Q(orderStoreName='京东九河泉仓库') |
                                       Q(orderStoreName='民生银行仓库')), ],

        '电视购物': [queryset_order.filter(orderStoreName='电视购物仓库'), ],
        '禾中农业': [queryset_order.filter(Q(orderStoreName='禾中农业仓库') |
                                       Q(orderStoreName='农业订单')),],
        '产品部': [queryset_order.filter(orderStoreName='产品部仓库'),],
    }


    if channal == 'B2B':
        queryset_list_c = choice_channal['B2B']
        choice_region = {
            '总部机构': [queryset_list_c[0].filter(Q(orderStoreName='北京仓库') | Q(orderStoreName='北京分仓')),],
            '华北大区': [queryset_list_c[0].filter(orderStoreName='天津仓库'),],
            '双鸭山分公司': [queryset_list_c[0].filter(orderStoreName='双鸭山仓库'),],
            '东北大区': [queryset_list_c[0].filter(orderStoreName='沈阳仓库'),],
            '华南大区': [queryset_list_c[0].filter(orderStoreName='深圳仓库'),],
            '西南大区': [queryset_list_c[0].filter(orderStoreName='成都仓库'),],
            '北方大区': [queryset_list_c[0].filter(orderStoreName='呼和浩特仓库'),],
            '华东大区': [queryset_list_c[0].filter(orderStoreName='上海仓库'),],
            '西北大区': [queryset_list_c[0].filter(orderStoreName='兰州仓库'),],
            '中原大区': [queryset_list_c[0].filter(orderStoreName='郑州仓库'),],
            '全部大区': [queryset_list_c[0],],
        }
        if region == '总部机构':
            queryset_list_r = choice_channal['总部机构']
            depot_choice = {
                '北京仓库': [queryset_list_r[0].filter(orderStoreName='北京仓库'),],
                '北京分仓': [queryset_list_r[0].filter(orderStoreName='北京分仓')],
                '全部配送中心': [queryset_list_r[0],],
            }
            if depot == '北京仓库':
                queryset_list_end = depot_choice['北京仓库']
            elif depot == '北京分仓':
                queryset_list_end = depot_choice['北京分仓']
            elif depot == '全部配送中心':
                queryset_list_end = depot_choice['全部配送中心']

        elif region == '华北大区':
            queryset_list_r = choice_channal['华北大区']
            depot_choice = {
                '天津仓库': [queryset_list_r[0],],
            }
            if depot == '天津仓库':
                queryset_list_end = depot_choice['天津仓库']

        elif region == '双鸭山分公司':
            queryset_list_r = choice_channal['双鸭山分公司']
            depot_choice = {
                '双鸭山仓库': [queryset_list_r[0].filter(orderStoreName='双鸭山仓库'), ],
            }
            if depot == '双鸭山仓库':
                queryset_list_end = depot_choice['双鸭山仓库']
        elif region == '东北大区':
            queryset_list_r = choice_channal['东北大区']
            depot_choice = {
                '沈阳仓库': [queryset_list_r[0].filter(orderStoreName='沈阳仓库'), ],
            }
            if depot == '沈阳仓库':
                queryset_list_end = depot_choice['沈阳仓库']
        elif region == '华南大区':
            queryset_list_r = choice_channal['华南大区']
            depot_choice = {
                '深圳仓库': [queryset_list_r[0].filter(orderStoreName='深圳仓库'), ],
            }
            if depot == '深圳仓库':
                queryset_list_end = depot_choice['深圳仓库']
        elif region == '西南大区':
            queryset_list_r = choice_channal['西南大区']
            depot_choice = {
                '成都仓库': [queryset_list_r[0].filter(orderStoreName='成都仓库'), ],
            }
            if depot == '成都仓库':
                queryset_list_end = depot_choice['成都仓库']
        elif region == '北方大区':
            queryset_list_r = choice_channal['北方大区']
            depot_choice = {
                '呼和浩特仓库': [queryset_list_r[0].filter(orderStoreName='呼和浩特仓库'), ],
            }
            if depot == '呼和浩特仓库':
                queryset_list_end = depot_choice['呼和浩特仓库']
        elif region == '华东大区':
            queryset_list_r = choice_channal['华东大区']
            depot_choice = {
                '上海仓库': [queryset_list_r[0].filter(orderStoreName='上海仓库'), ],
            }
            if depot == '上海仓库':
                queryset_list_end = depot_choice['上海仓库']
        elif region == '西北大区':
            queryset_list_r = choice_channal['西北大区']
            depot_choice = {
                '兰州仓库': [queryset_list_r[0].filter(orderStoreName='兰州仓库'), ],
            }
            if depot == '兰州仓库':
                queryset_list_end = depot_choice['兰州仓库']
        elif region == '中原大区':
            queryset_list_r = choice_channal['中原大区']
            depot_choice = {
                '郑州仓库': [queryset_list_r[0].filter(orderStoreName='郑州仓库'), ],
            }
            if depot == '郑州仓库':
                queryset_list_end = depot_choice['郑州仓库']
        elif region == '全部大区':
            queryset_list_end = choice_channal['全部大区']

        elif region == '华北大区':
            queryset_list = choice_channal['华北大区']
        elif region == '双鸭山分公司':
            queryset_list = choice_channal['双鸭山分公司']
        elif region == '东北大区':
            queryset_list = choice_channal['东北大区']
        elif region == '华南大区':
            queryset_list = choice_channal['华南大区']
        elif region == '西南大区':
            queryset_list = choice_channal['西南大区']
        elif region == '北方大区':
            queryset_list = choice_channal['北方大区']
        elif region == '华东大区':
            queryset_list = choice_channal['华东大区']
        elif region == '西北大区':
            queryset_list = choice_channal['西北大区']
        elif region == '中原大区':
            queryset_list = choice_channal['中原大区']
        elif region == '全部配送中心':
            queryset_list = choice_channal['西北大区']

    elif channal == 'B2C':
        queryset_list_c = choice_channal['B2C']
        # choice_region = {
        #     '总部机构': [queryset_list_c[0].filter(Q(orderStoreName='禾中便利店0001') | Q(orderStoreName='禾中便利店0002') | Q(orderStoreName='北京分仓') | Q(orderStoreName='直营门店') | Q(orderStoreName='北京分仓门店') | Q(orderStoreName='北京仓库')), ],
        #     '华北大区': [queryset_list_c[0].filter(Q(orderStoreName='天津仓库') | Q(orderStoreName='天津分仓门店')), ],
        #     '双鸭山分公司': [queryset_list_c[0].filter(Q(orderStoreName='双鸭山仓库') | Q(orderStoreName='双鸭山分仓门店')), ],
        #     '东北大区': [queryset_list_c[0].filter(Q(orderStoreName='沈阳仓库') | Q(orderStoreName='沈阳分仓门店')),],
        #     '华南大区': [queryset_list_c[0].filter(Q(orderStoreName='深圳仓库') | Q(orderStoreName='深圳分仓门店')),],
        #     '西南大区': [queryset_list_c[0].filter(orderStoreName='成都仓库'),],
        #     '北方大区': [queryset_list_c[0].filter(orderStoreName='呼和浩特仓库'), ],
        #     '华东大区': [queryset_list_c[0].filter(orderStoreName='上海仓库'), ],
        #     '西北大区': [queryset_list_c[0].filter(orderStoreName='兰州仓库'), ],
        #     '中原大区': [queryset_list_c[0].filter(orderStoreName='郑州仓库'), ],
        #     '全部大区': [queryset_list_c[0], ],
        # }
        if region == '总部机构':
            if depot == '禾中便利店0001':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='禾中便利店0001')]
            elif depot == '禾中便利店0002':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='禾中便利店0002')]
            elif depot == '北京分仓':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='北京分仓')]
            elif depot == '直营门店':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='直营门店')]
            elif depot == '北京分仓门店':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='北京分仓门店')]
            elif depot == '北京仓库':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='北京仓库')]
            else:
                queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='禾中便利店0001') | Q(orderStoreName='禾中便利店0002') | Q(orderStoreName='北京分仓') | Q(orderStoreName='直营门店') | Q(orderStoreName='北京分仓门店') | Q(orderStoreName='北京仓库'))]
        elif region == '华北大区':
            if depot == '天津仓库':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='天津仓库')]
            elif depot == '天津分仓门店':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='天津分仓门店')]
            else:
                queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='天津仓库') | Q(orderStoreName='天津分仓门店')), ]
        elif region == '双鸭山分公司':
            if depot == '双鸭山仓库':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='双鸭山仓库')]
            elif depot == '双鸭山分仓门店':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='双鸭山分仓门店')]
            else:
                queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='双鸭山仓库') | Q(orderStoreName='双鸭山分仓门店')), ]
        elif region == '东北大区':
            if depot == '沈阳仓库':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='沈阳仓库')]
            elif depot == '沈阳分仓门店':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='沈阳分仓门店')]
            else:
                queryset_list_end = [
                    queryset_list_c[0].filter(Q(orderStoreName='沈阳仓库') | Q(orderStoreName='沈阳分仓门店')), ]

        elif region == '华南大区':
            if depot == '深圳仓库':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='深圳仓库')]
            elif depot == '深圳分仓门店':
                queryset_list_end = [queryset_list_c[0].filter(orderStoreName='深圳分仓门店')]
            else:
                queryset_list_end = [queryset_list_c[0].filter(Q(orderStoreName='深圳仓库') | Q(orderStoreName='深圳分仓门店')), ]
        elif region == '西南大区':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='成都仓库'),]
        elif region == '北方大区':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='呼和浩特仓库'), ]
        elif region == '华东大区':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='成都仓库'), ]
        elif region == '西北大区':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='兰州仓库'), ]
        elif region == '中原大区':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='郑州仓库'), ]
        elif region == '全部大区':
            queryset_list_end = queryset_list_c


    elif channal == '电商渠道':
        queryset_list_c = choice_channal['电商渠道']
        if depot == '京东官方直营店':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='京东官方直营店')]
        elif depot == '京东九河泉仓库':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='京东九河泉仓库')]
        elif depot == '民生银行仓库':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='民生银行仓库')]
        else:
            queryset_list_end = queryset_list_c

    elif channal == '电视购物':
        queryset_list_end = choice_channal['电视购物']

    elif channal == '禾中农业':
        queryset_list_c = choice_channal['禾中农业']
        if depot == '禾中农业仓库':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='禾中农业仓库')]
        elif depot == '农业订单':
            queryset_list_end = [queryset_list_c[0].filter(orderStoreName='农业订单')]
        else:
            queryset_list_end = queryset_list_c

    elif channal == '产品部':
        queryset_list_end = choice_channal['产品部']
    else:
        queryset_list_end = choice_channal['全部渠道']

    if len(queryset_list_end) == 1:
        query = queryset_list_end[0]
        order_amount = query.aggregate(Sum('amount'))['amount__sum']

    elif len(queryset_list_end) == 2:
        query1 = queryset_list_end[0]
        query2 = queryset_list_end[1]

    pass



