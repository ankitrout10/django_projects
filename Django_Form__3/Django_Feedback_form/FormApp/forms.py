from django import forms

class Feedback(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=20)
    branch=forms.CharField(max_length=30)
    comments=forms.CharField(max_length=40)

    