from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from uprofile.models import Uprofile


def mine(request):
    return render(request, 'mine/mine.html', context={})


def mainAPI(request):
    ucellphone = request.session.get('ucellphone', None)
    profile_dic = model_to_dict(Uprofile.objects.get(ucellphone=ucellphone))
    choices_t = {
        1: '前端登录 总经理',
        2: '前端登录 副总经理',
        3: '前端登录 大区经理',
        4: '前端登录 产品部经理',
        5: '前端登录 北京招商部经理',
        6: '前端登录 北京招商部主管',
        7: '前端登录 北京招商部专员',
        8: '前端登录 直营事业部经理',
        9: '前端登录 电视直销部经理',
        10: '前端登录 电子商务部经理',
        11: '前端登录 数据分析人员',
        12: '前端登录 其他人员',

        100: '后台登录 上帝权限',# 上帝权限
        101: '后台登录 后台管理',# 无权
}

    check_choices = {
        1: '已审核',
        0: '待审核',
        -1: '审核未通过',
        -2: '已删除',
    }
    profile_dic['ustatus'] = check_choices[profile_dic['ustatus']]
    profile_dic['uposition'] = choices_t[profile_dic['uposition']][5::]
    return JsonResponse(profile_dic)
