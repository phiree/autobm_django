from django.shortcuts import render
from ..models import Supplier
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse

# Create your views here.
#字典管理



class SupplierList(ListView):
    model=Supplier
    template_name = 'car_service/siteadmin/supplier/supplier_list.html'


class SupplierCreate(CreateView):
    model=Supplier
    template_name = 'car_service/siteadmin/supplier/supplier_create.html'
    def get_success_url(self):
         return reverse('car_service:supplier_update',args=(self.object.id,))



class SupplierUpdate(UpdateView):
    model=Supplier
    template_name = 'car_service/siteadmin/supplier/supplier_update.html'

    def get_object(self, queryset=None):
        obj = Supplier.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:supplier_update',args=(self.object.id,))



