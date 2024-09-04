from django import forms

class Employee(forms.Form):
    eid=forms.IntegerField()
    name=forms.CharField(max_length=30)
    company=forms.CharField(max_length=30)
    age=forms.IntegerField()
    