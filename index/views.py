from django.shortcuts import render
from rest_framework.decorators import api_view

from .serializers import LoginSerializer

# Create your views here.
def login(request):
    return render(request, 'index/login.html', context={})

# @api_view(['POST', ])
# def login(request):
#     if request.method == "POST":
#         # queryset = models.
#         pass