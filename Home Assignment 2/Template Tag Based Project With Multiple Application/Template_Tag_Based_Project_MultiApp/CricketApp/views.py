from django.shortcuts import render

# Create your views here.
def mycricketviews(request):
    d={
        'name':'Virat Kohli', 'Centuries' : '80', 'runs': '15000' 
    }
    return render(request,'CricketApp/home.html',context=d)
