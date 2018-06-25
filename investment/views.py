import json, time, os

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers

import base64
import hmac

key  = "JD98Dskw=23njQndW9D"

def generate_token(key, expire=3600):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")

def certify_token(key, token):
    r'''
        @Args:
            key: str
            token: str
        @Returns:
            boolean
    '''
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True



def handle_upload_file(file, filename):
    basepath = 'static/media/investment_pic/'  # 上传文件的保存路径，可以自己指定任意的路径
    today = time.localtime()
    year = str(today.tm_year)
    mon = str(today.tm_mon)
    # day = str(today.tm_mday)\
    global path
    path = basepath+year+'/'+mon+'/'
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            pass
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# Create your views here.

@csrf_exempt
def verifylogin(request):
    '''post登录验证'''
    try:
        if request.method == 'POST':

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)  # 类型为<class 'django.contrib.auth.models.User'>

            if user:
                if user.username == 'hezhiqiang':
                    token = generate_token(key, 3600)
                    userinfo = {'username': 'hezhiqiang', 'power': 'check', 'token':token}
                    response = HttpResponse(json.dumps(userinfo), content_type='application/json')
                    response.set_cookie('token',token)
                    return response
                elif user.username == 'xiongshaohan':
                    token = generate_token(key, 3600)
                    userinfo = {'username': 'xiongshaohan', 'power': 'upload', 'token':token}
                    return HttpResponse(json.dumps(userinfo), content_type='application/json')
                    # response.set_cookie('token', token)
                    # return response
                else:
                    return HttpResponse('帐号、密码错误')
            return HttpResponse('错啦！！')
    except:
        return HttpResponse('大错特错！！')

# @login_required
@csrf_exempt
def dataupload(request):
    try:
        if request.method == 'POST':
            name = str(request.FILES['img']).split('.')

            filenm = 'xiongshaohan' + '-' + name[0] + '-' + str(
                time.strftime("%Y-%m-%d-%Hh%Mm%Ss", time.localtime())) + '.' + name[1]

            handle_upload_file(request.FILES['img'], filenm)
            models.sale_upload.objects.using('investment').create(createdate=request.POST.get('dates','none'),
                                                                  salesname=str(request.POST.get('clerk','none')),
                                                                  amount=int(request.POST.get('money','0')),
                                                                  imageurl=path+filenm,
                                                                  checkif=0,
                                                                  )
            handle_upload_file(request.FILES['img'], filenm)
            return HttpResponse(json.dumps({'result': 'successful'}), content_type='application/json')
    except:
        return HttpResponse(json.dumps({'result': 'faild'}), content_type='application/json')



# @login_required
@csrf_exempt
def checkdata(request):
    try:
        if request.method == 'GET':
            token = request.META.get('HTTP_AUTHORIZATION', 'asdf')
            if certify_token(key, token) and request.GET.get('power') == 'check':

                queryset = models.sale_upload.objects.using('investment').filter(checkif=0)
                serializer = serializers.sale_uploadSerializer(queryset, many=True)
                return HttpResponse(json.dumps(serializer.data), content_type='application/json')
    except:
        return HttpResponse('wrong')

# @login_required
@csrf_exempt
def checkif(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION', 'asdf')
        if certify_token(key, token):
            if request.method == 'POST' and request.POST.get('power') == 'check':
                id = int(request.POST.get('id'))
                checkif = int(request.POST.get('checkif'))
                dt = models.sale_upload.objects.using('investment').get(id=id)
                dt.checkif = checkif
                dt.save()
                return HttpResponse(json.dumps({'result': 'sucessful'}), content_type='application/json')
    except:
        return HttpResponse('wrong')