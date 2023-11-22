from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def msg(request):
    return HttpResponse('<h1>Welcome to Django<h1/>')
