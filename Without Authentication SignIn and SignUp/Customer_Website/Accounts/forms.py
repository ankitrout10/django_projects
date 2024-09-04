from typing import Any
from django import forms
from .models import User

class Register_Form(forms.ModelForm):
    password_confirm=forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=['username', 'password']
        widgets={
            'password':forms.PasswordInput(),

        }
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        password_confirm=cleaned_data.get('password_confirm')
        if password!=password_confirm:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

class Login_Form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')
        return cleaned_data
    
    