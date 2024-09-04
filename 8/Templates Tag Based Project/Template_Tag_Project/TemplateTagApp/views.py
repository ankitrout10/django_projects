from django.shortcuts import render

# Create your views here.
def home_view(request):
    name="SURENDRA"
    d={'n':name}
    return render(request,'TemplateTagApp/home.html',context=d)
