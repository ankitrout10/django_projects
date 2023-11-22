from django.contrib import admin
from django.urls import path
from TimeApp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('time/',views.displayTime)
]
