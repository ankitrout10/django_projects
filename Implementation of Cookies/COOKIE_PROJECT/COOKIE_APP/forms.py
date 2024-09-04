from django import forms

class Add_Product_Form(forms.Form):
    Product_Name = forms.CharField(max_length=30)
    Quantity = forms.IntegerField()
    