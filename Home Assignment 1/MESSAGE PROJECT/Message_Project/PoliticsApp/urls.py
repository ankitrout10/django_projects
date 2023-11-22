from django.contrib import admin
from django.urls import path
from PoliticsApp import views

urlpatterns = [
    path('hey/',views.mypoliticsviews ),
]