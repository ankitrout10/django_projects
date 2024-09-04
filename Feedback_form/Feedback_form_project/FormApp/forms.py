from django import forms

class Feedback(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=30)
    branch=forms.CharField(max_length=30)
    comment=forms.CharField(max_length=40)
    