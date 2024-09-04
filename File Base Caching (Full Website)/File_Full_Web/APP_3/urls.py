from django.urls import path
from .import views
urlpatterns = [
    path('haan/',views.home_view),
]