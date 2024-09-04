from django.shortcuts import render

# Create your views here.
def mymovieviews(request):
    d={
        'name':'Ranveer Singh', 'Movies' : '20', 'best': 'Padmavaat' 
    }
    return render(request,'MoviesApp/home.html',context=d)
