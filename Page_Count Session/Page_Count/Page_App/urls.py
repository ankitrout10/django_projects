from django.urls import path
from . import views
urlpatterns = [
    path('page_count/',views.page_count),
]
