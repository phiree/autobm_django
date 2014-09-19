from django.shortcuts import render
from ...models import Supplier,Service,ServiceDetail,Tree,ServicePropertyValue,ServicePropertyValue_Brand,ServicePropertyValue_Brand_FoilType
from django.views.generic import ListView,CreateView,UpdateView,View

from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理
from ..share.service import *
from django.forms.models import inlineformset_factory,modelform_factory


class ServicePropertyValueList(ListView):
    model=ServicePropertyValue
    template_name = 'car_service/site_admin/servicepropertyvalue/list.html'

class ServicePropertyValueCreate(CreateView):
    model=ServicePropertyValue
    template_name = 'car_service/site_admin/servicepropertyvalue/update_form.html'
    def get_success_url(self):
        return reverse('car_service:servicepropertyvalue_update',args=(self.object.id,))

def  servicepropertyvalue_create(request):
    return servicepropertyvalue_edit(request,None)
def  servicepropertyvalue_update(request,id):
    return servicepropertyvalue_edit(request,id)

def  servicepropertyvalue_edit(request,id):

    v_instance=None
    if id != None:
        v_instance=ServicePropertyValue.objects.get_subclass(pk=id)

    form_facory=modelform_factory(ServicePropertyValue)
    type=request.GET.get('type')
    if type=='b':
        form_facory=modelform_factory(ServicePropertyValue_Brand)
    if type=='f':
        form_facory=modelform_factory(ServicePropertyValue_Brand_FoilType)


    if v_instance!=None:
            form_facory=modelform_factory(v_instance.__class__)
    form=form_facory(instance=v_instance)
    if request.method=='POST':
        form=form_facory(request.POST,instance=v_instance)
        if form.is_valid():
            s_instance=form.save()
            return HttpResponseRedirect(reverse('car_service:servicepropertyvalue_update',args=( s_instance.id,)))
    return render(request, 'car_service/site_admin/servicepropertyvalue/update_form.html',
                  {'form': form,})



class ServicePropertyValueUpdate(UpdateView):
    model=ServicePropertyValue
    template_name = 'car_service/site_admin/servicepropertyvalue/update_form.html'

    def get_object(self, queryset=None):
        obj = ServicePropertyValue.objects.get(id=self.kwargs['id'])
        if obj.brand is not None:
            obj=obj.servicepropertyvalue_brand
        if obj.foiltype is not None:
            obj=obj.servicepropertyvalue_band_foiltype
        return obj
    def get_success_url(self):
         return reverse('car_service:servicepropertyvalue_update',args=(self.object.id,))



