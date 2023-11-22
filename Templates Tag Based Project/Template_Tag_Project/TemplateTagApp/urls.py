from django.contrib import admin
from django.urls import path
from TemplateTagApp import views
urlpatterns = [
    path('msg/', views.home_view),

]
