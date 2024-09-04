from django.shortcuts import render
from .models import Student
# Create your views here.
def get_all_records(request):
    records= Student.objects.all()
    d = {'records': records}
    return render(request,'Student_App/home.html',d)

def get_specific_record(request,id):
    record= Student.objects.get(pk=id)
    d = {'record': record}
    return render(request,'Student_App/card.html',d)

