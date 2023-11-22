from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def displayTime(request):
    dt=datetime.datetime.now()
    t=dt.strftime("%H:%M:%S")
    hour=int(t[:2])
    result=''

    if hour>=00 and hour<=4:
        result='Good Night'
    elif hour>=5 and hour<12:
        result='Good Morning'
    elif hour>=12 and hour<4:
        result='Good Afternoon'
    else:
        result='Good Night'
    return HttpResponse(result) 
               
