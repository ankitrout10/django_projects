from django.contrib import admin
from .models import Task_Details
# Register your models here.

@admin.register(Task_Details)
class Task_Details_Admin(admin.ModelAdmin):
    list_display = ['id', 'Task_name', 'Task_status']
    