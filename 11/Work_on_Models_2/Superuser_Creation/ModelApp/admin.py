from django.contrib import admin
from ModelApp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','name','company']

admin.site.register(Employee,EmployeeAdmin)

