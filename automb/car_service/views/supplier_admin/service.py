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

'''
商家后台
服务项目管理 : 列表,查看
订单管理
资料管理

'''
def index(request):
    return render(request,'car_service/supplier_admin/index.html')
    pass
def service_list(request):

    supplier=Supplier.objects.get(owner=request.user)
    service_detail_list=ServiceDetail.objects.filter(service__supplier=supplier)
    service_child_list=Service.objects.filter(id__in=service_detail_list.values('service_id'))
    service_type_child_list=Tree.objects.filter(id__in=service_child_list.values('service_type_id'))
    service_type_top_list=Tree.objects.filter(id__in=service_type_child_list.values('parent_id'))
    service_type=request.GET.get('service_type')
    if service_type:
        service_detail_list=service_detail_list.filter(service__service_type__name=service_type)
    return render(request,'car_service/supplier_admin/service_list.html'
    ,{'top_service_types':service_type_top_list,'object_list':service_detail_list})

class ServiceList(ListView):
    model=ServiceDetail
    template_name ='car_service/supplier_admin/service_list.html'
    pass

def create(request):

    pass
def update(request,id):

    pass



