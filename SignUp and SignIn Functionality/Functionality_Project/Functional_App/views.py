from django.shortcuts import render,HttpResponseRedirect
from .models import Visitor
from .forms import Visitor_form,vm_form

# Create your views here.
def my_view(request):
    return render(request,'Functional_App/home.html')

def visitor_to(request):
    if request.method == 'POST':
        form=vm_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/Functional_App/success/')
    form=vm_form()
    d={'form': form}
    return render(request,'Functional_App/sign_up.html',d)

def success_view(request):
    return render(request,'Functional_App/success.html')


def visitor_view(request):
    # create for Visitor_form class
    if request.method == 'POST':
        form=Visitor_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/Functional_App/end/')
    form=Visitor_form()
    d={'form': form}
    return render(request,'Functional_App/sign_in.html',d)

def end_view(request):
    return render(request,'Functional_App/end.html')
    

