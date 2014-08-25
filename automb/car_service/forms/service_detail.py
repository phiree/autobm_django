from django.forms import ModelForm
from ..models import ServiceDetail,Service
__author__ = 'Administrator'
from django import forms

class ServiceDetailForm(ModelForm):

    class Meta:
        model=ServiceDetail
        exclude=('service',)

class ServiceForm(ModelForm):
    class Meta:
        model=Service
        widgets={
            'car':forms.CheckboxSelectMultiple()
        }