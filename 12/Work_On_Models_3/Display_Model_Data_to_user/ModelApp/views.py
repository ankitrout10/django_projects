from django.shortcuts import render
from ModelApp.models import Employee
# Create your views here.
def employee_data(request):
    l=Employee.objects.all()
    d={'data':l}
    return render (request,'ModelApp/home.html',context=d)
