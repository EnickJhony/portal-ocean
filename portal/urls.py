from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
