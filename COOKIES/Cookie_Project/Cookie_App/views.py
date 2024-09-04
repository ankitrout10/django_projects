from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_cookie_view(request):
    response =HttpResponse('Cookie is set')
    response.set_cookie(key='name',value='Ankit',max_age=60*60*24*365)
    return response

def get_cookie_view(request):
    name = request.COOKIES['name']
    return HttpResponse(name)

def delete_cookie_view(request):
    response =HttpResponse('Cookie deleted')
    response.delete_cookie('name')
    return response
