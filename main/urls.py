"""IDcard_Payments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^studentvieworadd/', views.SViewOrAdd.as_view()),
    url(r'^studentmodordelete/', views.SModOrDelete.as_view()),
    # url(r'^drivervieworadd/', views.DViewOrAdd.as_view()),
    # url(r'^drivermodordelete/', views.DModOrDelete.as_view()),
    # url(r'^cabvieworadd/', views.CViewOrAdd.as_view()),
    # url(r'^cabmodordelete/', views.CModOrDelete.as_view()),
    # url(r'^cabhisvieworadd/', views.CHViewOrAdd.as_view()),
    # url(r'^cabhisdelete/', views.CHDelete.as_view()),
    # url(r'^payhisvieworadd/', views.PHViewOrAdd.as_view()),
    # url(r'^payhismodordelete/', views.PHModOrDelete.as_view()),
    # url(r'^travhisvieworadd/', views.THViewOrAdd.as_view()),
    # url(r'^travhismodordelete/', views.THMoodOrDelete.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)