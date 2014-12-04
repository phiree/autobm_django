from django.shortcuts import render
from django.forms.models import inlineformset_factory
from ...models import Supplier ,Service2,ServiceValue
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理
from ..share.service import *
from ...biz import service2 as biz_service2

class ServiceList(ListView):
    model=Service2
    template_name = 'car_service/site_admin/service2/service_list.html'

#used in both site_admin and supplier_admin
class ServiceUpdate(UpdateView):
    model=Service2
    template_name = 'car_service/site_admin/service2/update_form.html'

    def get_object(self, queryset=None):
        obj = Service2.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:site_admin_service2_update',args=(self.object.id,))

class ServiceCreate(CreateView):
    model=Service2
    template_name = 'car_service/site_admin/service2/update_form.html'
    def get_success_url(self):
        return reverse('car_service:site_admin_service2_update',args=(self.object.id,))

def update_value(request,service_id):
    service,values=biz_service2.update_service_value(request.method,request.POST,service_id)
    return render(request,'car_service/site_admin/servicevalue/update_form.html', {"service":service,'values':values })




