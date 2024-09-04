from django import forms
from django.core import validators

class Student(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField()
    age=forms.IntegerField()
    branch=forms.CharField()

def clean(self):
    data= super().clean()
    sid = data['sid']
    name = data['name']
    age = data['age']
    branch = data['branch']

    if 


