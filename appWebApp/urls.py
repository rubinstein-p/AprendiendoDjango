from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from appWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', views.home, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)