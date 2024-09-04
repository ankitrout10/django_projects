from django.shortcuts import HttpResponse,render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def redg_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration is Successfull')
        else:
            return HttpResponse('Please enter valid data')
    form = UserCreationForm()
    return render(request,'App/redg_form.html',{'form':form})

