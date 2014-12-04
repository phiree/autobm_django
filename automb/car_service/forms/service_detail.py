from django.forms import ModelForm
from ..models import  ServiceValue,Service2,Supplier
__author__ = 'Administrator'
from django import forms



class Service2Form(ModelForm):
    class Meta:
        model=Service2
        fields=['supplier','servicetype']
    def __init__(self,*args,**kwargs):

        super(Service2Form,self).__init__(*args,**kwargs)
        #


class ServiceValueForm(ModelForm):
    class Meta:
        model=ServiceValue
        exclude=('service',)

