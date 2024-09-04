from django.shortcuts import render
from FormApp.forms import Feedback
# Create your views here.

def feedback_view(request):
    f=Feedback()
    d={'form':f}
    if request.method=='POST':
        data=Feedback(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            comment=data.cleaned_data['comment']
            return render(request,'FormApp/thankyou.html',{'name':name , 'comment':comment})

    return render(request,'FormApp/home.html',context=d)
    
