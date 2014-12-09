from django.forms import ModelForm,Form
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

class Service2ValueForm(Form):
    pass

class Service2HtmlForm(Form):
    title=forms.CharField(max_length=100)
    


