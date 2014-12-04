from django.core.exceptions import ValidationError
from django.forms import ModelForm

__author__ = 'Administrator'
from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(max_length=100,required=False)
    def clean_email(self):

        email=self.cleaned_data['email']
        if not email:
            return ''
        if len(email)<10:
            raise ValidationError('email format maybe wrong')
        return email


    def clean_password2(self):
        password=self.cleaned_data['password']
        password2=self.cleaned_data['password2']
        if password!=password2:
            raise ValueError('passwords not same')
        return password2

