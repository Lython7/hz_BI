from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'auth/', views.login_auth),

]
