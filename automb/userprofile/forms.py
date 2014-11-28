__author__ = 'Administrator'
from django import forms
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=("real_name",'gender','phone','email')
