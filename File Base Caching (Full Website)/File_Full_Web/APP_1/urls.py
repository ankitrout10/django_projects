from django.urls import path
from .import views

urlpatterns = [
    path('h1/',views.home_view),
    
]