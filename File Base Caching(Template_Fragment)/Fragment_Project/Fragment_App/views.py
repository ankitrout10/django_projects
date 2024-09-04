from django.shortcuts import render

# Create your views here.
def virat_view(request):
    return render(request,'Fragment_App/virat.html')
def rohit_view(request):
    return render(request,'Fragment_App/rohit.html')
def bumrah_view(request):
    return render(request,'Fragment_App/bumrah.html')
