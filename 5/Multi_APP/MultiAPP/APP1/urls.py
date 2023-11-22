from django.contrib import admin
from django.urls import path
# from views import *
from APP1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first1/',views.msg),
    path('first2/',views.printMe)
]
