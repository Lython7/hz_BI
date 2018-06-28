from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mine, name='mine'),
    url(r'^profile/$', views.mainAPI, name='mainAPI'),

]