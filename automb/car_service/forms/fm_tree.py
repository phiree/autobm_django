from django.forms import ModelForm
from ..models import ServiceDetail,Service,Tree
__author__ = 'Administrator'
from django import forms

class TreeForm(ModelForm):
    class Meta:
        model=Tree


