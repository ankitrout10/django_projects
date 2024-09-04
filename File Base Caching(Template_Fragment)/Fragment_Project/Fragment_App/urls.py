from django.urls import path
from .import views

urlpatterns = [
    path('virat/',views.virat_view),
    path('rohit/',views.rohit_view),
    path('bumrah/',views.bumrah_view),
    
]
