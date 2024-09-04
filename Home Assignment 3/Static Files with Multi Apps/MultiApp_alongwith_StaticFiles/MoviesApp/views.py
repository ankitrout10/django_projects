from django.shortcuts import render

# Create your views here.
def mymovies_view(request):
    d = {
        'name':'Ranveer Singh', 'Movies':'20', 'best':'83'
    }
    return render(request,'MoviesApp/home.html',context=d)

