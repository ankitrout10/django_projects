from django.shortcuts import render
from FormApp.forms import Employee
# Create your views here.

def employee_view(request):
    f=Employee()
    d={'form':f}
    if request.method=='POST':
        f1=Employee(request.POST)
        if f1.is_valid():
            print(f'{f1.cleaned_data['eid']}')
            print(f'{f1.cleaned_data['name']}')
            print(f'{f1.cleaned_data['comapny']}')
            print(f'{f1.cleaned_data['age']}')
            d={'form':f1}
            return render(request,'FormApp/home.html',context=d)
    return render(request,'FormApp/home.html',context=d)


