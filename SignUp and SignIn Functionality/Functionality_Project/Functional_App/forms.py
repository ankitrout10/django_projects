from django import forms
from .models import Visitor

class Visitor_form(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()

class vm_form(forms.ModelForm):
    class Meta:
        model=Visitor
        fields='__all__'
            