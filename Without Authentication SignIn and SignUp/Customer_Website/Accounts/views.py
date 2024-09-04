from django.shortcuts import render,redirect
from .forms import Register_Form
from .models import User
from .forms import Login_Form

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = Register_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')

    else:
        form=Register_Form()
    return render(request,'Accounts/register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=Login_Form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=user.objects.get(username=username,password=password) 
            request.session['user_id']=user.id # Store the user ID in the session.
            username=user.username
            return render(request,'Accounts/dashboard.html',{'username':username})
    else:
        form=Login_Form()
    return render(request,'Accounts/login.html',{'form':form})

def dashboard_view(request):
    if request.session.get('user_id',False):
        id=request.session['user_id']
        user=User.objects.get(id=id)
        username=user.username
        return render(request,'Accounts/dashboard.html',{'username':username})
    else:
        return redirect('login')
    
def logout_view(request):
    del request.session['user_id']
    return redirect('login')
    
            