from django.contrib import admin
from django.urls import path
from MoviesApp import views

urlpatterns = [
    path('hi/',views.mymovies_view ),
]
