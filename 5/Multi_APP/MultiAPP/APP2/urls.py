from django.contrib import admin
from django.urls import path
from APP2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('second1/',views.msg),
    path('second2/',views.printYou)
]
