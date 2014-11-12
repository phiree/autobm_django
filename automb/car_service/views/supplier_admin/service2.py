from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.forms.models import inlineformset_factory
from ...models import Supplier,Service,ServiceDetail,Tree,Service2,ServiceValue,ServicePropertyValue
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse
from ...forms import service_detail,fm_supplier_admin_supplier_create
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
# Create your views here.
#字典管理
from ..share.service import *
from ...biz import service2 as biz_service2
from ...decorators import group_required

class ServiceList(ListView):
    @method_decorator(login_required)
    @method_decorator(group_required('supplier'))
    def dispatch(self, *args, **kwargs):
        return super(ServiceList, self).dispatch(*args, **kwargs)
    model=Service2
    template_name = 'car_service/supplier_admin/service_list.html'
    def get_queryset(self):
        return Service2.objects.filter(supplier__owner=self.request.user)

class ServiceUpdate(UpdateView):
    model=Service2
    form_class = service_detail.Service2Form
    template_name = 'car_service/supplier_admin/update_form.html'
    def get_object(self, queryset=None):
        obj = Service2.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:supplier_admin_servicevalue_update',args=(self.object.id,))

class ServiceCreate(CreateView):
    model=Service2
    form_class = service_detail.Service2Form
    template_name = 'car_service/supplier_admin/update_form.html'
    def get_success_url(self):
        return reverse('car_service:supplier_admin_servicevalue_update',args=(self.object.id,))
    def get_form(self, form_class):
        form = super(ServiceCreate,self).get_form(form_class)
        form.fields['supplier'].queryset=Supplier.objects.filter(owner=self.request.user)


        return form
def edit_service2(request,service_id):

    instance=Service2()
    if service_id:
        instance=Service2.objects.get(pk=service_id)
    form_service=service_detail.Service2Form(instance=instance)
    form_value=service_detail.ServiceValueForm(instance=instance.service)
    if request.method=='POST':
        pass



def update_value(request,service_id):
    service,values=biz_service2.update_service_value(request.method,request.POST,service_id)
    return render(request,'car_service/supplier_admin/servicevalue_update_form.html', {"service":service,'values':values })


class SupplierUpdate(UpdateView):
    form_class = fm_supplier_admin_supplier_create.SupplierCreateForm
    template_name = 'car_service/supplier_admin/supplier_form.html'
    def get_object(self, queryset=None):
        return Supplier.objects.get(id=self.kwargs['supplier_id'])
    def get_success_url(self):
        return reverse('car_service:supplier_admin_supplier_create_success',args=(self.object.id,))


class SupplierCreate(CreateView):
    model=Supplier
    form_class = fm_supplier_admin_supplier_create.SupplierCreateForm
    template_name='car_service/supplier_admin/supplier_form.html'
    def get_success_url(self):
        return reverse('car_service:supplier_admin_supplier_create_success',args=(self.object.id,))
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super(SupplierCreate, self).form_valid(form)
class SupplierList(ListView):
    model=Supplier
    template_name = 'car_service/supplier_admin/supplier_list.html'
    def get_queryset(self):
        return Supplier.objects.filter(owner=self.request.user)

def supplier_create_success(request,supplier_id):
    return render(request,'car_service/supplier_admin/supplier_form_success.html')


