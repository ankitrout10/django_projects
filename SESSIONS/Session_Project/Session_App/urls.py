from django.urls import path
from .import views

urlpatterns = [
    path('set_session/',views.create_session),
    path('get_session/',views.get_session),
    # path('delete_session/',views.delete_session),
    path('page_count/',views.page_count),

]