from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'APP_3/home.html')

