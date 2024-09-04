from django.contrib import admin
from django.urls import path
from StaticFilesApp import views

urlpatterns = [
    path('home/', views.home_view),
    
]
