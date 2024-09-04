from django.shortcuts import render

import datetime
import calendar
# Create your views here.
def mycricket_view(request):
    d={
        'name': 'Virat Kohli', 'Centuries': '79', 'runs':'15000', 'time':displayTime() , 'date':displaydate(), 'day':displayday()
    }
    return render(request,'CricketApp/home.html',context=d)
def displayTime():
    dt=datetime.datetime.now()
    t=dt.strftime("%H:%M:%S")
    hour=int(t[:2])
    result=''

    if hour>=00 and hour<=4:
        result='Good Night'
    elif hour>4 and hour<12:
        result='Good Morning'
    elif hour>=12 and hour<16:
        result='Good Afternoon'
    else:
        result='Good Evening'
    return (result) 
def displaydate():
    c= datetime.date.today()
    t=c.strftime("%d/%m/%Y")  
    return t

def displayday():
    # a= datetime.date.weekday(datetime.date.today())
    a= datetime.datetime.now().weekday()
    wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return wd[a]


           
           
