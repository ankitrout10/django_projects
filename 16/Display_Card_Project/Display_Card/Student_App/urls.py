
from django.urls import path
from .import views

urlpatterns = [
    path('get_all_records/',views.get_all_records),
    path('<int:id>/', views.get_specific_record,name='card')
    

]
