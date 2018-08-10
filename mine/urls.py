from django.conf.urls import url
from django.templatetags.static import static
from hz_BI import settings
from . import views

urlpatterns = [
    url(r'^$', views.mine, name='mine'),
    url(r'^profile/$', views.mainAPI, name='mainAPI'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)