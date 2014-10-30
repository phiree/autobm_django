from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.forms.models import inlineformset_factory
from ...models import Supplier,Service,ServiceDetail,Tree,Service2,ServiceValue,ServicePropertyValue
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
# Create your views here.
#字典管理
from ..share.service import *
from ...biz import service2 as biz_service2


class ServiceList(ListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ServiceList, self).dispatch(*args, **kwargs)
    model=Service2
    template_name = 'car_service/supplier_admin/service_list.html'

class ServiceUpdate(UpdateView):
    model=Service2
    template_name = 'car_service/supplier_admin/update_form.html'
    def get_object(self, queryset=None):
        obj = Service2.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:supplier_admin_service2_update',args=(self.object.id,))

class ServiceCreate(CreateView):
    model=Service2
    template_name = 'car_service/supplier_admin/update_form.html'
    def get_success_url(self):
        return reverse('car_service:supplier_admin_service2_update',args=(self.object.id,))

def update_value(request,service_id):
    service,values=biz_service2.update_service_value(request.method,request.POST,service_id)
    return render(request,'car_service/supplier_admin/servicevalue_update_form.html', {"service":service,'values':values })



