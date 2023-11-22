from django.contrib import admin
from django.urls import path
from CricketApp import views
urlpatterns = [
    path('hello/', views.mycricketviews),
]