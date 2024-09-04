from django.urls import path
from FormApp import views

urlpatterns = [
    path('feedback_form/',views.feedback_view),
    
]