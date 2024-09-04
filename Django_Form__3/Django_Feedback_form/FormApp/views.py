from django.shortcuts import render
from FormApp.forms import Feedback
# Create your views here.

def feedback_view(request):
    f=Feedback()
    d={{'form':f}}
    if request.method=='POST':
        data=Feedback(request.POST)
        if data.is_valid():
            print(f'Sid is: {data.cleaned_data['sid']}')
            print(f'Name is: {data.cleaned_data['name']}')
            print(f'Branch is: {data.cleaned_data['branch']}')
            print(f'Comment is: {data.cleaned_data['comment']}')
            return render(request,'FormApp/thankyou.html')
    return render(request,'FormApp/home.html',context=d)
    
            
