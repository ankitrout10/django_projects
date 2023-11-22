from django.shortcuts import render

# Create your views here.
def mypoliticsviews(request):
    return render(request,'PoliticsApp/home.html')
    