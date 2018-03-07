import os, time

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import xlrd, json
from rest_framework import viewsets

from . import serializers, models


class ExcelToJson(object):
    # def __init__(self, host="localhost", user="root", passwd="2531", db="hz_BI"):
    #     # 连接数据库
    #     database = pymysql.connect(host=host, user=user, passwd=passwd, db="hz_BI")
    #     cursor = database.cursor()
    def __init__(self, filename, sheetname):
        self.datalist = []
        self.filename = filename
        self.sheetname = sheetname

    def readExcel(self):
        # 获取excelData文件夹中上传了的excel文件
        try:
            excelFile = xlrd.open_workbook('../media/yoback/excelData/' + self.filename)
            sheet = excelFile.sheet_by_name(self.sheetname)
            for i in range(1,sheet.nrows):
                dic = {}
                for j in range(sheet.ncols):
                    dic[sheet.cell(0,j)] = sheet.cell(i,j)
                self.datalist.append(dic)
        except:
            print('excel读取过程中有问题')

    def jsonhandle(self):
        if self.datalist:
            jsonstr = json.dumps(self.datalist)
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

@login_required
def yoback(request):
    return render(request, 'yoback/yoback.html')

@login_required
def upload(request):
    if request.method == "POST":
        name = str(request.FILES['xlfile']).split('.')
        filenm = request.user.username + '-' + name[0] + str(time.strftime("%Y-%m-%d-%Hh%Mm%Ss",time.localtime())) + '.' + name[1]
        handle_upload_file(request.FILES['xlfile'], filenm)
        return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中

    # return render_to_response('course/upload.html')


def handle_upload_file(file, filename):
    path = 'media/yoback/excelData/'  # 上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

