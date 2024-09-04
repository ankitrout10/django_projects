from django.shortcuts import render

# Create your views here.
def mypoliticalviews(request):
    d={
        'name':'Narendra Modi', 'Party' : 'BJP', 'Elections': '2024' 
    }
    return render(request,'PoliticsApp/home.html',context=d)
