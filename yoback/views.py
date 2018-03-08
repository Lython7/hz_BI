import os, time
from hz_BI.settings import MEDIA_ROOT

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
import xlrd, json
from rest_framework import viewsets

from . import serializers, models


class ExcelToJson(object):
    # def __init__(self, host="localhost", user="root", passwd="2531", db="hz_BI"):
    #     # 连接数据库
    #     database = pymysql.connect(host=host, user=user, passwd=passwd, db="hz_BI")
    #     cursor = database.cursor()
    def __init__(self, filename):
        self.datadictotal = {}
        self.datalist = []
        self.filename = filename


    def readExcel(self):
        # 获取excelData文件夹中上传了的excel文件
        # try:
        excelFile = xlrd.open_workbook(os.path.join(MEDIA_ROOT+'/yoback/excelData', self.filename))


        for sheet in excelFile.sheets():
            for i in range(sheet.nrows):
                dic = {}
                for j in range(sheet.ncols):
                    dic[sheet.cell(0, j).value] = sheet.cell(i, j).value
                self.datalist.append(dic)
            self.datadictotal[sheet.name] = self.datalist
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
        # return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中

        # 开始读excel
        data = ExcelToJson(filenm)
        datadic = data.readExcel()
        # datadictotal = {'data': datadic}

        return render(request, 'yoback/excelcheck.html', context={'datadic':datadic})
        # return JsonResponse({'data':datals})

    # return render_to_response('course/upload.html')


def handle_upload_file(file, filename):
    path = 'media/yoback/excelData/'  # 上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

