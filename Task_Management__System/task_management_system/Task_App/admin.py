from django.contrib import admin
from .models import Task_Details
# Register your models here.

@admin.register(Task_Details)
class Task_details_admin(admin.ModelAdmin):
    list_display=['Task_name','Task_status']
    