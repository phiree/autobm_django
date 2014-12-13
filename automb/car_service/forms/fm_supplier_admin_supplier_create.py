from django.forms import ModelForm
from ..models import Supplier
__author__ = 'Administrator'
from django import forms

class SupplierCreateForm(ModelForm):
    class Meta:
        model=Supplier
        exclude=['owner','promote_code']
    def __init__(self, *args, **kwargs):
        super(SupplierCreateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['promote_code'].widget.attrs['disabled'] = 'disabled'




