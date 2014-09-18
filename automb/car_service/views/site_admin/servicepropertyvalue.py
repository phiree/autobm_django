from django.shortcuts import render
from ...models import Supplier,Service,ServiceDetail,Tree,ServicePropertyValue
from django.views.generic import ListView,CreateView,UpdateView,View

from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理
from ..share.service import *
from django.forms.models import inlineformset_factory


class ServicePropertyValueList(ListView):
    model=ServicePropertyValue
    template_name = 'car_service/site_admin/servicepropertyvalue/list.html'

class ServicePropertyValueCreate(CreateView):
    model=ServicePropertyValue
    template_name = 'car_service/site_admin/servicepropertyvalue/update_form.html'
    def get_success_url(self):
        return reverse('car_service:servicepropertyvalue_update',args=(self.object.id,))


class ServicePropertyValueUpdate(UpdateView):
    model=ServicePropertyValue
    template_name = 'car_service/site_admin/servicepropertyvalue/update_form.html'

    def get_object(self, queryset=None):
        obj = ServicePropertyValue.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:servicepropertyvalue_update',args=(self.object.id,))



