from django.contrib import admin
from django.urls import path
from My_Website import views
urlpatterns = [
    path('msg/', views.home_view),
    
]
