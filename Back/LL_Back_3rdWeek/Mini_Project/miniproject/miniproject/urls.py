from django.contrib import admin
from django.urls import path, include
from MiniApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('youtube/', views.youtube, name = 'youtube'),
]