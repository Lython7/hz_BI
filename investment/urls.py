from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^loginvf/', views.verifylogin),
    url(r'^upload/', views.dataupload),
    url(r'^check/', views.checkdata),
    url(r'^checkif/', views.checkif),


]