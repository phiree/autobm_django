from django.shortcuts import render
from django.forms.models import inlineformset_factory
from ...models import Supplier,Service,ServiceDetail,Tree,Service2,ServiceValue
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理
from ..share.service import *


class ServiceList(ListView):
    model=Service2
    template_name = 'car_service/site_admin/service2/service_list.html'


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


def service_create(request):
    return service_create_update(request,None)

def service_update(request,id):
    return service_create_update(request,id)

def service_create_update(request,id):
    is_new= True if id==None else False
    if not is_new:
        instance_service=Service2.objects.get(pk=id)
    else:
        instance_service=Service2()
    ServiceValueFormSet=inlineformset_factory(Service2,ServiceValue)
    if request.method =='POST':

        fm_service=service_detail.Service2Form(request.POST,instance=instance_service)
        instance_service= fm_service.save()
        fms_service=ServiceValueFormSet(instance=instance_service)
        if fms_service.is_valid():
            instance_service=fm_service.save()
            return HttpResponseRedirect(reverse('car_service:site_admin_service2_update',args=(instance_service.id,)))
    else:
        fm_service=fm_service=service_detail.Service2Form(instance=instance_service)
        fms_service=ServiceValueFormSet(instance=instance_service)
    return render(request,'car_service/site_admin/service2/service_update.html',
        {
            'fms_service':fms_service,
            'fm_service':fm_service
        })

def edit(request,id):
    fm_service,fm_service_detail=service_edit(request,id)
    if fm_service.is_valid() and fm_service_detail.is_valid():
        return HttpResponseRedirect(reverse('car_service:site_admin_service_edit',args=(fm_service_detail.instance.id,)))
    return render(request,'car_service/site_admin/service/service_edit.html',
                    {
                        'fm_service_detail':fm_service_detail,
                        'fm_service':fm_service
                    }
                  )


