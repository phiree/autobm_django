from django.forms import ModelForm
from ..models import ServiceDetail,Service,ServiceValue,Service2
__author__ = 'Administrator'
from django import forms

class ServiceDetailForm(ModelForm):

    class Meta:
        model=ServiceDetail
        exclude=('service',)
        widgets={
            'car':forms.CheckboxSelectMultiple()
        }
class ServiceForm(ModelForm):
    class Meta:
        model=Service

class Service2Form(ModelForm):
    class Meta:
        model=Service2


class ServiceValueForm(ModelForm):
    class Meta:
        model=ServiceValue
        exclude=('service',)

