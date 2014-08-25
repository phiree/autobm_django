from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from ...models import Supplier,Service,ServiceDetail,Tree
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理

def index(request):
    return  render(request,'car_service/supplier_admin/index.html')

class ServiceList(ListView):
    model=ServiceDetail
    template_name = 'car_service/site_admin/service/service_list.html'

def service_edit(request,id):
    is_new= True if id==None else False
    if not is_new:
        instance_service_detail=ServiceDetail.objects.get(pk=id)
        instance_service=instance_service_detail.service
    else:
        instance_service_detail=ServiceDetail()
        instance_service=Service()
    if request.method =='POST':
        fm_service_detail=service_detail.ServiceDetailForm(request.POST,instance=instance_service_detail)
        fm_service=service_detail.ServiceForm(request.POST,instance=instance_service)
        if fm_service.is_valid() and fm_service_detail.is_valid():
            try:
                instance_service=Service.objects.get(service_type=fm_service.instance.service_type,supplier=fm_service.instance.supplier)
            except ObjectDoesNotExist:
                instance_service=fm_service.save()
            instance_service_detail = fm_service_detail.save(commit=False)
            instance_service_detail.service=instance_service
            instance_service_detail.save()

            #return HttpResponseRedirect(reverse('car_service:service_update',args=(instance_service_detail.id,)))
    else:
        fm_service_detail=service_detail.ServiceDetailForm(instance=instance_service_detail)
        fm_service=service_detail.ServiceForm(instance=instance_service)

    return (fm_service,fm_service_detail)
    '''return render(request,'car_service/site_admin/service/service_edit.html',
        {
            'fm_service_detail':fm_service_detail,
            'fm_service':fm_service
        })'''




