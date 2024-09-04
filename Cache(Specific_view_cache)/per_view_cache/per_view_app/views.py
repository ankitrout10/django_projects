from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(120)
def home_view(request):
    return render(request,'per_view_app/home.html')
def contact_view(request):
    return render(request,'per_view_app/contact.html')
def about_view(request):
    return render(request,'per_view_app/about.html')

