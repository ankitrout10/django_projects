from django.shortcuts import render

# Create your views here.
def mycricketviews(request):
    return render(request,'CricketApp/home.html')
    