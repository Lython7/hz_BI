import os, time

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response

from rest_framework import viewsets

from . import serializers, models
from uprofile import models as umodels
from .excelhandle import *


def checkexcel(request):
    return render(request, 'yoback/excelcheck.html', context={})

class GoodsClassifyViewSet(viewsets.ModelViewSet):
    queryset = models.GoodsClassify.objects.all()
    serializer_class = serializers.GoodsClassifySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    # pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# @login_required
def yoback(request):
    if request.user.is_authenticated and request.user.is_staff == 1:
        return render(request, 'yoback/yoback.html', context={})
    else:
        return HttpResponseRedirect('/login')

@login_required
def upload(request):
    # 如何是电商或者god 则可用进入  否则提示无权限！ 同理建设电视的上传
    power = umodels.Uprofile.objects.get(user=request.user).upower
    if power == 1 or power == 3:
        if request.method == "POST":

            name = str(request.FILES['xlfile']).split('.')
            filenm = request.user.username + '-' + name[0] + '-' + str(time.strftime("%Y-%m-%d-%Hh%Mm%Ss",time.localtime())) + '.' + name[1]
            handle_upload_file(request.FILES['xlfile'], filenm)
            request.session['filenm'] = filenm

            # 开始读excel
            data = ExcelToJson(filenm)
            datadic = data.readExcel()
            # datadictotal = {'data': datadic}

            return render(request, 'yoback/excelcheck.html', context={'datadic':datadic})

        if request.method == "GET":

            filenm = request.session.get('filenm', None)
            if  filenm:
                data = ExcelToJson(filenm)
                datadic = data.readExcel()

                # keyName = filenm.split('-')[1]
                if '商品清单' in filenm:
                    # ******************************************************************
                    # ******************************************************************
                    for i in datadic['商品分类'][1::]:
                        models.GoodsClassify.objects.create(catNo= i['catNo'],
                                                            catName= i['catname'],
                                                            edited_by= request.user)
                    # ******************************************************************
                    # ******************************************************************

                    for i in datadic['商品清单'][1::]:
                        models.GoodsList.objects.create(channel= i['渠道'],
                                                        catNo= models.GoodsClassify.objects.get(catNo=i['分类编码']),
                                                        skuNo=str(i['sku编码']),
                                                        skuName=i['sku名称'],
                                                        price=i['商品单价'],
                                                        edited_by= request.user)
                    # ******************************************************************
                    # ******************************************************************
                elif '退货' in filenm:

                    for i in datadic['退货订单'][1::]:
                        models.RevokeOrder.objects.create(channel= i['渠道'],
                                                        rorderdate= i['退货日期'],
                                                        rordertime=i['退货时间'],
                                                        rorderNo=i['退货订单号'],
                                                        orderNo=i['原始订单号'],
                                                        skuNo=i['sku编码'],
                                                        ramount=i['退货数量'],
                                                        price=i['商品单价'],
                                                        discountprice=i['折扣金额'],
                                                        revokeprice=i['退货商品金额'],
                                                        rorderPay=i['退货订单金额'],

                                                        edited_by= request.user)
                    # ******************************************************************
                    # ******************************************************************
                else:
                    try:
                        for i in datadic['销售订单'][1::]:
                            models.SaleOrder.objects.create(channel= i['渠道'],
                                                            orderdate= i['下单日期'],
                                                            ordertime=i['下单时间'],
                                                            orderNo=i['订单号'],
                                                            customer=i['客户姓名'],
                                                            cuscellphone=i['联系方式'],
                                                            province=i[r'省/市'],
                                                            city=i[r'市/区'],
                                                            skuNo=i['sku编码'],
                                                            amount=i['数量'],
                                                            price=i['商品单价'],
                                                            Sumprice=i['商品总金额'],
                                                            discountprice=i['折扣金额'],
                                                            orderPay=i['订单实付金额'],
                                                            promotion=i['促销活动'],
                                                            edited_by= request.user)
                    except:
                        print('表不对！')


                return JsonResponse({'url': '/yoback/'})
            else:
                return JsonResponse({'error': '审核失败，请核查excel内容，重新上传！,请检查是否有新商品需要添加。'})
    else:
        return HttpResponse('无权限访问')


