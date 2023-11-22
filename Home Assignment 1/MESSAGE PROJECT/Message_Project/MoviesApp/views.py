from django.shortcuts import render

# Create your views here.
def mymovieviews(request):
    return render(request,'MoviesApp/home.html')
    