from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home_view),
    path('about/',views.about_view),
    path('contact/',views.contact_view),
    
]



