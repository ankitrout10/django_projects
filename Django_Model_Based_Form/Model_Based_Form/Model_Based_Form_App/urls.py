from django.urls import path
from .import views
urlpatterns = [
    path('redg/',views.redg_view),
    path('thankyou/',views.thankyou_view)

    
    
]