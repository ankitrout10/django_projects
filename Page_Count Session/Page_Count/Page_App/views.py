from django.shortcuts import render,HttpResponse

# Create your views here.
def page_count(request):
    count=request.session.get('count',0)
    newcount=count+1
    c=request.session['count']=newcount
    return HttpResponse(c)
