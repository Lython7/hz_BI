from django.conf.urls import url
from django.templatetags.static import static
from hz_BI import settings
from . import views

urlpatterns = [
    url(r'^$', views.explore, name='explore'),
    url(r'^exploreAPI', views.explore_API, name='explore_API'),
    url(r'^goodscount_2', views.goodscount_2, name='goodscount_2'),
    url(r'^goodscount', views.goodscount, name='goodscount'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)