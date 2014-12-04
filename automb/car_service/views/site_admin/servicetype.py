from django.shortcuts import render
from ...models import Supplier ,ServiceType
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


class ServiceTypeList(ListView):
    model=ServiceType
    template_name = 'car_service/site_admin/servicetype/list.html'
    def get_queryset(self):
        return ServiceType.objects.filter(parent=None)

class ServiceTypeCreate(CreateView):
    model=ServiceType
    template_name = 'car_service/site_admin/servicetype/update_form.html'
    def get_success_url(self):
        return reverse('car_service:servicetype_update',args=(self.object.id,))


class ServiceTypeUpdate(UpdateView):
    model=ServiceType
    template_name = 'car_service/site_admin/servicetype/update_form.html'

    def get_object(self, queryset=None):
        obj = ServiceType.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:servicetype_update',args=(self.object.id,))



