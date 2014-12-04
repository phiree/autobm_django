from django.forms import ModelForm
from ..models import Supplier
__author__ = 'Administrator'
from django import forms

class SupplierCreateForm(ModelForm):
    class Meta:
        model=Supplier
        exclude=['owner']
    def __init__(self,*args,**kwargs):

        super(SupplierCreateForm,self).__init__(*args,**kwargs)
        #self.fields['supplier'].queryset=Supplier.objects.filter(owner=self.request.user)



