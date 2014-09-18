from django.shortcuts import render
from ...models import Supplier,Service,ServiceDetail,Tree,ServiceProperty
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


class ServicePropertyList(ListView):
    model=ServiceProperty
    template_name = 'car_service/site_admin/serviceproperty/list.html'

class ServicePropertyCreate(CreateView):
    model=ServiceProperty
    template_name = 'car_service/site_admin/serviceproperty/update_form.html'
    def get_success_url(self):
        return reverse('car_service:serviceproperty_update',args=(self.object.id,))


class ServicePropertyUpdate(UpdateView):
    model=ServiceProperty
    template_name = 'car_service/site_admin/serviceproperty/update_form.html'

    def get_object(self, queryset=None):
        obj = ServiceProperty.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:serviceproperty_update',args=(self.object.id,))



