from django.contrib import admin
from django.urls import path, include
from youtube import views

urlpatterns = [
    path('',views.youtube, name = 'youtubepage'),
    path('1/', views.one, name = 'first'),
    path('2/', views.two, name = 'second'),
    path('3/', views.three, name = 'third'),


]