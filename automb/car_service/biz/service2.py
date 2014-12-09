from django.shortcuts import render
from django.forms.models import inlineformset_factory
from ..models import Supplier, Service2,ServiceValue,ServicePropertyValue,UserComment,Bill
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理

#used in both site_admin and supplier_admin

def update_service_value(request_method,request_post_data,service_id):
    service=Service2.objects.get(pk=service_id)

    values=service.servicevalue_set.values_list('servicepropertyvalue__id',flat=True)

    if request_method=="POST":
        selected=request_post_data
        service.servicevalue_set.all().delete()
        for v in request_post_data:
            if 'option' in v:
                selected_value=request_post_data.get(v)
                spv=ServicePropertyValue.objects.get(pk=int(selected_value))

                sv=ServiceValue(service=service,servicepropertyvalue=spv)
                sv.save()
        service.price=request_post_data.get('price')
        service.price_market=request_post_data.get('price_market')
        service.save()
    return (service,values)

def get_comment_status(request,service_id):
    result={'status':None,'comment':None,'bill':None}
    status_choice=((0,'已评论'),(1,'已购买未评论'),(2,'未购买'),(3,'未登录'))
    if  not request.user.is_active:
        result['status']=status_choice[3]
        return result
    comment_list=UserComment.objects.filter(bill__service__id=service_id)
    status=None
    if comment_list.count()==0:
        bill_list=Bill.objects.filter(service__id=service_id, user__id=request.user.id)
        if bill_list.count()==1:
            result['status']=status_choice[1]
            result['bill']=bill_list[0]
        else:
            result['status']=status_choice[2]
    else:
        result['status']=status_choice[0]
        result['comment']=comment_list[0]
    return result




