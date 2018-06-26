import time

from django.db.models import Q

from hzyg.models import *


class incomeDay(object):
    '''营收数据'''

    def _get_settings(self, request):
        # 获取今日营收权限
        return request.session.get('settings')

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

    def _get_month(self):
        return time.strftime("%Y-%m", time.localtime()).split('-')

    def _get_queryset_list(self, request, year, month, day, _settings=0):
        # 获取queryset
        querysetlist = []
        if month == None and day == None:
            queryset1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year)
            queryset2 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year)
            queryset3 = b2b_store.objects.using('hzyg').filter(status=0, createDate__year=year)
            queryset4 = b2b_goodstable.objects.using('hzyg').filter(createDate__year=year)

        elif month and day == None:
            queryset1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)
            queryset2 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)
            queryset3 = b2b_store.objects.using('hzyg').filter(status=0, createDate__year=year, createDate__month=month)
            queryset4 = b2b_goodstable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month)

        else:
            queryset1 = b2b_ordertable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)
            queryset2 = b2b_posgoods.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)
            queryset3 = b2b_store.objects.using('hzyg').filter(status=0, createDate__year=year, createDate__month=month, createDate__day=day)
            queryset4 = b2b_goodstable.objects.using('hzyg').filter(createDate__year=year, createDate__month=month, createDate__day=day)

        if _settings == 0:
            pass

        elif _settings == 1:
            querysetlist.append(queryset1)
            querysetlist.append(queryset2)
            querysetlist.append(queryset3)
            querysetlist.append(queryset4)

        elif _settings == 2:
            # 电商数据 京东官方直营店1013 民生银行仓库101014 九河泉101106
            querysetlist.append(queryset1.filter(Q(orderStore='1013') | Q(orderStore='101014') | Q(orderStore='101106')))
            querysetlist.append(queryset2.filter(Q(orderStore=1013) | Q(orderStore=101014) | Q(orderStore=101106)))
            querysetlist.append(queryset3.filter(Q(storeCode='1013') | Q(storeCode='101014') | Q(storeCode='101106')))
            querysetlist.append(queryset4.filter(Q(storeCode='1013') | Q(storeCode='101014') | Q(storeCode='101106')))

        elif _settings == 3:
            # 电视购物数据 101103
            querysetlist.append(queryset1.filter(orderStore='101103'))
            querysetlist.append(queryset2.filter(orderStore=101103))
            querysetlist.append(queryset3.filter(storeCode='101103'))
            querysetlist.append(queryset4.filter(storeCode='101103'))

        elif _settings == 4:#
            # B2B数据全部                               1010                  1011                         101101                 101102                  1012                      1016                 102101                    103101                   104101                    105101                  106101                   107101                   108101              109101               110101
            querysetlist.append(queryset1.filter(Q(orderStore='1010') | Q(orderStore='1011') | Q(orderStore='101101') | Q(orderStore='101102') | Q(orderStore='1012') | Q(orderStore='1016') | Q(orderStore='102101') | Q(orderStore='103101') | Q(orderStore='104101') | Q(orderStore='105101') | Q(orderStore='106101') | Q(orderStore='107101') | Q(orderStore='108101') | Q(orderStore='109101') | Q(orderStore='110101')))
            # querysetlist.append(queryset2.filter(Q(orderStore=1010)   | Q(orderStore=1011)   |                          Q(orderStore=101102)   | Q(orderStore=1012)   | Q(orderStore=1016)   | Q(orderStore=102101)   | Q(orderStore=103101)   | Q(orderStore=104101)   | Q(orderStore=105101)   | Q(orderStore=106101)   | Q(orderStore=107101)   | Q(orderStore=108101)   | Q(orderStore=109101)   | Q(orderStore=110101)))
            querysetlist.append(queryset2.filter(orderStore=4124312))
            querysetlist.append(queryset3.filter(Q(storeCode='1010')  | Q(storeCode='1011')  | Q(storeCode='101101')  | Q(storeCode='101102')  | Q(storeCode='1012')  | Q(storeCode='1016')  | Q(storeCode='102101')  | Q(storeCode='103101')  | Q(storeCode='104101')  | Q(storeCode='105101')  | Q(storeCode='106101')  | Q(storeCode='107101')  | Q(storeCode='108101')  | Q(storeCode='109101')  | Q(storeCode='110101')))
            querysetlist.append(queryset4.filter(Q(storeCode='1010')  | Q(storeCode='1011')  | Q(storeCode='101101')  | Q(storeCode='101102')  | Q(storeCode='1012')  | Q(storeCode='1016')  | Q(storeCode='102101')  | Q(storeCode='103101')  | Q(storeCode='104101')  | Q(storeCode='105101')  | Q(storeCode='106101')  | Q(storeCode='107101')  | Q(storeCode='108101')  | Q(storeCode='109101')  | Q(storeCode='110101')))

        elif _settings == 15:
            # 直营店1014
            querysetlist.append(queryset1.filter(orderStore='1014'))
            querysetlist.append(queryset2)
            querysetlist.append(queryset3.filter(storeCode='1014'))
            querysetlist.append(queryset4.filter(storeCode='1014'))


        elif _settings == 16:
            # 禾中农业 禾中农业仓库 101105 农业订单 1015
            querysetlist.append(queryset1.filter(Q(orderStore='101105') | Q(orderStore='1015')))
            querysetlist.append(queryset2.filter(Q(orderStore=101105) | Q(orderStore=1015)))
            querysetlist.append(queryset3.filter(Q(storeCode='101105') | Q(storeCode='1015')))
            querysetlist.append(queryset4.filter(Q(storeCode='101105') | Q(storeCode='1015')))

        elif _settings == 17:
            # 禾中味道  1201
            querysetlist.append(queryset1.filter(orderStore='1201'))
            querysetlist.append(queryset2.filter(orderStore=1201))
            querysetlist.append(queryset3.filter(storeCode='1201'))
            querysetlist.append(queryset4.filter(storeCode='1201'))

        elif _settings == 5:
            # 北京全部数据                             1010                  1011                         101101                 101102                  1012                      1016
            querysetlist.append(queryset1.filter(Q(orderStore='1010') | Q(orderStore='1011') | Q(orderStore='101101') | Q(orderStore='101102') | Q(orderStore='1012') | Q(orderStore='1016')))
            querysetlist.append(queryset2.filter(Q(orderStore=1010)   | Q(orderStore=1011)   | Q(orderStore='101101') | Q(orderStore=101102)   | Q(orderStore=1012)   | Q(orderStore=1016)))
            querysetlist.append(queryset3.filter(Q(storeCode='1010')  | Q(storeCode='1011')  | Q(storeCode='101101')  | Q(storeCode='101102')  | Q(storeCode='1012')  | Q(storeCode='1016')))
            querysetlist.append(queryset4.filter(Q(storeCode='1010')  | Q(storeCode='1011')  | Q(storeCode='101101')  | Q(storeCode='101102')  | Q(storeCode='1012')  | Q(storeCode='1016')))

        elif _settings == 6:
            # 华北数据 102101
            querysetlist.append(queryset1.filter(Q(orderStore='102101')))
            querysetlist.append(queryset2.filter(Q(orderStore=102101)))
            querysetlist.append(queryset3.filter(Q(storeCode='102101')))
            querysetlist.append(queryset4.filter(Q(storeCode='102101')))

        elif _settings == 7:
            # 双鸭山数据 103101
            querysetlist.append(queryset1.filter(Q(orderStore='103101')))
            querysetlist.append(queryset2.filter(Q(orderStore=103101)))
            querysetlist.append(queryset3.filter(Q(storeCode='103101')))
            querysetlist.append(queryset4.filter(Q(storeCode='103101')))

        elif _settings == 8:
            # 东北数据 104101
            querysetlist.append(queryset1.filter(Q(orderStore='104101')))
            querysetlist.append(queryset2.filter(Q(orderStore=104101)))
            querysetlist.append(queryset3.filter(Q(storeCode='104101')))
            querysetlist.append(queryset4.filter(Q(storeCode='104101')))

        elif _settings == 9:
            # 华南数据 105101
            querysetlist.append(queryset1.filter(Q(orderStore='105101')))
            querysetlist.append(queryset2.filter(Q(orderStore=105101)))
            querysetlist.append(queryset3.filter(Q(storeCode='105101')))
            querysetlist.append(queryset4.filter(Q(storeCode='105101')))


        elif _settings == 10:
            # 西南数据 106101
            querysetlist.append(queryset1.filter(Q(orderStore='106101')))
            querysetlist.append(queryset2.filter(Q(orderStore=106101)))
            querysetlist.append(queryset3.filter(Q(storeCode='106101')))
            querysetlist.append(queryset4.filter(Q(storeCode='106101')))

        elif _settings == 11:
            # 北方数据 107101
            querysetlist.append(queryset1.filter(Q(orderStore='107101')))
            querysetlist.append(queryset2.filter(Q(orderStore=107101)))
            querysetlist.append(queryset3.filter(Q(storeCode='107101')))
            querysetlist.append(queryset4.filter(Q(storeCode='107101')))


        elif _settings == 12:
            # 华东数据 108101
            querysetlist.append(queryset1.filter(Q(orderStore='108101')))
            querysetlist.append(queryset2.filter(Q(orderStore=108101)))
            querysetlist.append(queryset3.filter(Q(storeCode='108101')))
            querysetlist.append(queryset4.filter(Q(storeCode='108101')))

        elif _settings == 13:
            # 西北数据 109101
            querysetlist.append(queryset1.filter(Q(orderStore='109101')))
            querysetlist.append(queryset2.filter(Q(orderStore=109101)))
            querysetlist.append(queryset3.filter(Q(storeCode='109101')))
            querysetlist.append(queryset4.filter(Q(storeCode='109101')))


        elif _settings == 14:
            # 中原数据 110101
            querysetlist.append(queryset1.filter(Q(orderStore='110101')))
            querysetlist.append(queryset2.filter(Q(orderStore=110101)))
            querysetlist.append(queryset3.filter(Q(storeCode='110101')))
            querysetlist.append(queryset4.filter(Q(storeCode='110101')))

        elif _settings == 18:
            # 产品部 110107
            # print(len(queryset1.filter(Q(orderStore='110107'))))
            querysetlist.append(queryset1.filter(Q(orderStore='101107')))
            querysetlist.append(queryset2.filter(Q(orderStore=101107)))
            querysetlist.append(queryset3.filter(Q(storeCode='101107')))
            querysetlist.append(queryset4.filter(Q(storeCode='101107')))

        return querysetlist

