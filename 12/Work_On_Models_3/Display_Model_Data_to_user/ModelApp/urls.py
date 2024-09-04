from django.urls import path
from ModelApp import views
urlpatterns = [
    path('emp_data/', views.employee_data),
    
]
