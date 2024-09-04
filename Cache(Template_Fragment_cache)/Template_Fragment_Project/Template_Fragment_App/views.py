from django.shortcuts import render

# Create your views here.
def bhubaneswar_view(request):
    return render(request,'Template_Fragment_App/bhubaneswar.html')
def konark_view(request):
    return render(request,'Template_Fragment_App/konark.html')
def puri_view(request):
    return render(request,'Template_Fragment_App/puri.html')
