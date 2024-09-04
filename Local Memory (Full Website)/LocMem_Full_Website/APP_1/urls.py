from django.urls import path
from .import views
urlpatterns = [
    path('yes/',views.home_view),
    
]