from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ch1, name='ch1'),
]