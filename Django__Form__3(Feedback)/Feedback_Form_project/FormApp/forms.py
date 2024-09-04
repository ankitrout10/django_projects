from django import forms

class Feedback(forms.Feedback):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=20)
    branch=forms.CharField(max_length=20)
    comment=forms.CharField(max_length=40)
    