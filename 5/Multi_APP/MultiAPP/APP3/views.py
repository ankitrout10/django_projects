from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msg(request):
    return HttpResponse('<h2>Hello I am from APP3</h2>')

def printThank(request):
    return HttpResponse('<h2>Thank You</h2>')
