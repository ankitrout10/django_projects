from django.urls import path
from . import views

urlpatterns = [
    path('set_cookie/', views.set_cookie_view),
    path('get_cookie/',views.get_cookie_view),
    path('delete_cookie/',views.delete_cookie_view),
    
]
