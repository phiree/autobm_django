from django.forms import ModelForm
from ..models import  ServiceValue,Service2,Supplier
__author__ = 'Administrator'
from django import forms



class Service2Form(ModelForm):
    class Meta:
        model=Service2
        fields=['supplier','servicetype']



class ServiceValueForm(ModelForm):
    class Meta:
        model=ServiceValue
        exclude=('service',)

