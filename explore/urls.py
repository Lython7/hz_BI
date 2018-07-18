from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.explore, name='explore'),
    url(r'^exploreAPI', views.explore_API, name='explore_API'),
    url(r'^goodscount_2', views.goodscount_2, name='goodscount_2'),

]