from django.urls import path
from .import views

urlpatterns = [
    path('bbsr/',views.bhubaneswar_view),
    path('kon/',views.konark_view),
    path('puri/',views.puri_view),
    
]
