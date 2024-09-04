from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.my_view),
    path('visitor/',views.visitor_view,name='visitor'),
    path('end/',views.end_view),
    path('success/',views.success_view),
    path('visit/',views.visitor_to,name='visit'),



]
