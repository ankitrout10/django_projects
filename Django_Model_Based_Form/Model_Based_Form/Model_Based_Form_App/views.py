from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import RedgForm
from .models import RedgModel
# Create your views here.
def redg_view(request):
    if request.method=='POST':
        form=RedgForm(request.POST)
        if form.is_valid():
            return HttpResponsePermanentRedirect('/Model_Based_Form_App/thankyou/')
    form=RedgForm()
    d={'form': form}
    return render(request,'Model_Based_Form_App/redg.html',d)

def thankyou_view(request):
    return render(request,'Model_Based_Form_App/thankyou.html')
    