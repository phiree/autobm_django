from django.shortcuts import render
from django.contrib.auth.decorators import  login_required

from ...models import Supplier, Service2,ServiceValue,ServicePropertyValue,ServiceType

from ...forms import service_detail,fm_supplier_admin_supplier_create,fm_service2

from django.utils.decorators import method_decorator
# Create your views here.
#字典管理
from ..share.service import *
from ...biz import service2 as biz_service2
from ...decorators import group_required
from django.forms.models import inlineformset_factory,ModelForm,modelform_factory
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
def create_select_type(request):
    top_type_list=ServiceType.objects.filter(parent=None)
    return render(request,'car_service/supplier_admin/service_create_select_type.html',{'top_type_list':top_type_list})

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
#创建
def create_service2(request,type_id):
    return edit_service2(request,None,type_id)
#修改
def edit_service2(request,service_id):
    return edit_service2(request,service_id,None)


def edit_service2(request,service_id,type_id=None):

    service2=Service2()
    if service_id:
        service2=Service2.objects.get(pk=service_id)
        type_id=service2.servicetype.id
    supplier_list=request.user.supplier_set.all()

    service_type=ServiceType.objects.get(pk=type_id)
    service_value_id_list=service2.servicevalue_set.values_list('id',flat=True)
    errmsg=''
    if request.method=='POST':
        selected_supplier=Supplier.objects.get(pk=int(request.POST.get('supplier')))
        service_value_list_with_spv=[]
        servicepropertyvalue_list=[]
        exists_service_type=Service2.objects.filter(servicetype__id=type_id)
        for v in request.POST:
            if 'sel_' in v:
                selected_value=request.POST.get(v)
                spv=ServicePropertyValue.objects.get(pk=int(selected_value))
                servicepropertyvalue_list.append(spv)
                service_value=service2.servicevalue_set.filter(service__supplier__id=selected_supplier.id, servicepropertyvalue__id=int(selected_value))
                service_value_list_with_spv.append((service_value,spv))

        is_exists=True
        if len(exists_service_type)==0:
            is_exists=False
        else:
            for sv in service_value_list_with_spv:
                if sv[0].count()==0:
                    is_exists=False
                    break
        if service_id ==None and is_exists:
            #todo. 找出这个service,并直接更新
            errmsg='exists'
        else:
            service2.price=request.POST.get('price')
            service2.price_market=request.POST.get('price_market')
            service2.disabled=bool( request.POST.get('disabled'))
            service2.description=request.POST.get('description')
            service2.title=request.POST.get('title')
            service2.supplier=selected_supplier
            service2.servicetype=service_type
            service2.save()
            for sv in service_value_list_with_spv:
                if sv[0].count()==0:
                    service_value=ServiceValue(service=service2,servicepropertyvalue=sv[1])
                else:
                    service_value=sv[0][0]
                #service2.servicevalue_set.add(service_value)
                service_value.save()
            return HttpResponseRedirect(reverse('car_service:supplier_admin_service2_update',
                                                args=(service2.id,)
            ))

        pass

    return render(request,'car_service/supplier_admin/service_edit.html',
                  {'supplier_list':supplier_list,'service_type':service_type,
                   'service2':service2,
                   'service_value_id_list':service_value_id_list,
                   'errmsg':errmsg})

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

from unique_random.models import UniqueRandom
class SupplierCreate(CreateView):
    model=Supplier
    form_class = fm_supplier_admin_supplier_create.SupplierCreateForm
    template_name='car_service/supplier_admin/supplier_form.html'
    def get_success_url(self):
        return reverse('car_service:supplier_admin_supplier_create_success',args=(self.object.id,))
    def form_valid(self, form):
        form.instance.owner=self.request.user
        unique_random=UniqueRandom()
        unique_random.save()

        form.instance.promote_code=unique_random.code
        return super(SupplierCreate, self).form_valid(form)
class SupplierList(ListView):
    model=Supplier
    template_name = 'car_service/supplier_admin/supplier_list.html'
    def get_queryset(self):
        return Supplier.objects.filter(owner=self.request.user)

def supplier_create_success(request,supplier_id):
    return render(request,'car_service/supplier_admin/supplier_form_success.html')

