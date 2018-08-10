from django.conf.urls import url
from . import views
from django.templatetags.static import static
from hz_BI import settings

urlpatterns = [
    url(r'^loginvf/', views.verifylogin),
    url(r'^upload/', views.dataupload),
    url(r'^check/', views.checkdata),
    url(r'^checkif/', views.checkif),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)