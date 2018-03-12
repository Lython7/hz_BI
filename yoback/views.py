import os, time
from hz_BI.settings import MEDIA_ROOT
from datetime import datetime
from xlrd import xldate_as_tuple

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
import xlrd, json
from rest_framework import viewsets

from . import serializers, models


def handle_upload_file(file, filename):
    path = 'media/yoback/excelData/'  # 上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class ExcelToJson(object):
    # def __init__(self, host="localhost", user="root", passwd="2531", db="hz_BI"):
    #     # 连接数据库
    #     database = pymysql.connect(host=host, user=user, passwd=passwd, db="hz_BI")
    #     cursor = database.cursor()
    def __init__(self, filename):
        self.datadictotal = {}
        # self.datalist = []
        self.filename = filename

    def readExcel(self):
        # 获取excelData文件夹中上传了的excel文件
        # try:
        excelFile = xlrd.open_workbook(os.path.join(MEDIA_ROOT+'/yoback/excelData', self.filename))

        for sheet in excelFile.sheets():
            datalist = []
            for i in range(sheet.nrows):
                dic = {}
                for j in range(sheet.ncols):
                    if sheet.cell(i, j).ctype==3:
                        # xlrd.xldate.xldate_as_datetime(table.cell(2, 2).value, 1)
                        x = xlrd.xldate_as_datetime(sheet.cell(i, j).value, 0)
                        if int(sheet.cell(i, j).value) > 0:
                            # print(x)
                            # print(type(x))

                            dic[sheet.cell(0, j).value] = x.strftime('%Y-%d-%m')
                        else:
                            dic[sheet.cell(0, j).value] = x.strftime('%H:%M:%S')
                    else:
                        dic[sheet.cell(0, j).value] = sheet.cell(i, j).value
                datalist.append(dic)
            self.datadictotal[sheet.name] = datalist
        return self.datadictotal
        # except:
        #     print('excel读取过程中有问题')

    def jsonhandle(self):
        if self.datadictotal:
            jsonstr = json.dumps(self.datadictotal)
            return jsonstr
        else:
            print('json化失败！！')
            return None

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
        return HttpResponseRedirect('/login/')

@login_required
def upload(request):
    if request.method == "POST":
        name = str(request.FILES['xlfile']).split('.')
        filenm = request.user.username + '-' + name[0] + str(time.strftime("%Y-%m-%d-%Hh%Mm%Ss",time.localtime())) + '.' + name[1]
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
            print(datadic['商品分类'])
            # 写入数据库
            for i in datadic['商品分类'][1::]:
                models.GoodsClassify.objects.create(i)


def checkexcel(request):
    return render(request, 'yoback/excelcheck.html', context={})

