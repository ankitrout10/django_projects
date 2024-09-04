from django.shortcuts import render,HttpResponse,redirect
from .forms import Add_Product_Form

# Create your views here.
def home_view(request):
    if request.method =='POST':
        form=Add_Product_Form(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['Product_Name']
            quantity = form.cleaned_data['Quantity']
            response = redirect('home')
            response.set_cookie(product_name,quantity)
    else:
        form=Add_Product_Form()
        response=render(request,'COOKIE_APP/home.html',{'form':form})
    return response

def dispalay_cart_view(request):
    all_record=request.COOKIES
    context={
        'all_record':all_record,
    }
    return render(request,'COOKIE_APP/cart.html',context)

