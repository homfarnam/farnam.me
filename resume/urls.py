from django.contrib import admin
from django.urls import path , include , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('', views.index, name="index"),
    re_path('blog/',include('blog.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)