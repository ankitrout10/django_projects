from django.urls import path
from FormApp import views

urlpatterns = [
    path('emp_form/',views.employee_view),
    
]