from django.shortcuts import render
from FormApp.forms import Employee
# Create your views here.
def employee_view(request):
    f=Employee()
    d={'form':f}
    return render(request,'FormApp/home.html',context=d)

