from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from hzyg import models


def test(request):
    # data = models.b2b_goodstable.objects.using('hzyg').all()
    data = models.b2b_goodstable.objects.using('hzyg').filter(createDate__gt='2018-03-01')
    x = []
    for i in data:
        x.append(i.orderNo)
    # data = models.b2b_ordertable.objects.using('hzyg').all()
    x = str(x)
    return HttpResponse(x)


