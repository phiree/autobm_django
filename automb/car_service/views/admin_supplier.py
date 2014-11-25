from django.shortcuts import redirect

__author__ = 'Administrator'
from django.http import  HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView,DetailView
from ..models import Supplier,Bill,Service2

def home(request):
    return redirect(reverse('car_service:supplier_admin_service2_list'))

class BillList(ListView):
    model = Bill
    template_name = 'car_service/supplier_admin/bill_list.html'
    def get_queryset(self):
        bill_list= Bill.objects.filter(service__supplier__owner=self.request.user)
        return bill_list

class BillDetail(DetailView):
    model = Bill
    template_name = 'car_service/supplier_admin/bill_detail.html'
    slug_field = 'id'
    slug_url_kwarg ='bill_id'
import json

def complete_bill(request,bill_id):
    bill=Bill.objects.get(pk=bill_id)
    if bill.service.supplier.owner!=request.user:
        data={'result':False,'errmsg':'错误:没有权限'}
    if bill.status=='complete':
        data={'result':False,'errmsg':'错误:已经结单'}
    else:
        data={'result':True}
        bill.status='complete'
        bill.save()
    return HttpResponse(json.dumps(data),content_type='application/json')
def change_bill_status(request,target_status):
    pass
