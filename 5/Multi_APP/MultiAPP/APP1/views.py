from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msg(request):
    return HttpResponse('<h2>Hello I am from APP1</h2>')
def printMe(request):
    return HttpResponse('<h2>Hello</h2>')
