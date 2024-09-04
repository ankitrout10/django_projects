from django.urls import path
from . import views

urlpatterns = [

    path('hi/',views.home_view),
    
]
