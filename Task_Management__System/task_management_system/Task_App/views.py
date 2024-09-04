from django.shortcuts import render,redirect,get_object_or_404
from .models import Task_Details
# Create your views here.
def home_view(request):
    incompleted_task=Task_Details.objects.filter(task_status=False)
    completed_task=Task_Details.objects.filter(task_status=True)
    d = {
        'incompleted_task': incompleted_task,
        'completed_task': completed_task,

    }
    return render (request,'Task_App/urls',d)
def add_task(request):
    task_data=request.POST['add_task']
    Task_Details.objects.create(task_name=task_data)
    return redirect('home')

def undo_task(request,id):
    record=get_object_or_404(Task_Details,id=id)
    record.task_status=False
    record.save()
    return redirect('home')

def done_task(request,id):
    record=get_object_or_404(Task_Details,id=id)
    record.task_status=True
    record.save()
    return redirect('home')
     