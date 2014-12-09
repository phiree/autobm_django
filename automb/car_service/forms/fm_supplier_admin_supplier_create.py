from django.forms import ModelForm
from ..models import Supplier
__author__ = 'Administrator'
from django import forms

class SupplierCreateForm(ModelForm):
    class Meta:
        model=Supplier
        exclude=['owner']



