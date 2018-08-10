from django.conf.urls import url
from django.urls import path, include
from . import views
from django.templatetags.static import static
from hz_BI import settings

urlpatterns = [
    # url(r'^$', views.yoback, name='yoback'),

    # url(r'sendsms/(?P<cellphone>\d{11})$', demo_sms_send.send_sms, name='sendsms'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)