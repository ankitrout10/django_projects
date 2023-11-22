from django.contrib import admin
from django.urls import path
from TemplatesApp import views

urlpatterns = [
    path('msg/',views.my_views),
]
