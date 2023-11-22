from django.contrib import admin
from django.urls import path
from APP3 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('third1/',views.msg),
    path('third2/',views.printThank)
]
