from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home_view),
    path('add_task/', views.add_task,name='add_task'),
    path('undo_task/<int:id>', views.undo_task,name='undo_task'),
    path('done_task/<int:id>', views.done_task,name='done_task'),
]
    
