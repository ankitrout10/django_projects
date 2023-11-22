from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msg(request):
    return HttpResponse('<h2>Hello I am APP2</h2>')

def printYou(request):
    return HttpResponse('<h2>Hi</h2>')
