from django.shortcuts import render
from django.forms.models import inlineformset_factory
from ..models import Supplier,Service,ServiceDetail,Tree,Service2,ServiceValue,ServicePropertyValue
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





