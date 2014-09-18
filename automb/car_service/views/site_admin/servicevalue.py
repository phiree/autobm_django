from django.shortcuts import render
from ...models import Supplier,Service,ServiceDetail,Tree,ServiceType,Service2,ServiceValue,ServicePropertyValue
from django.views.generic import ListView,CreateView,UpdateView,View
import decimal
from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理
from ..share.service import *
from django.forms.models import inlineformset_factory

def update_value(request,service_id):
    service=Service2.objects.get(pk=service_id)

    values=service.servicevalue_set.values_list('servicepropertyvalue__id',flat=True)

    if request.method=="POST":
        selected=request.POST
        service.servicevalue_set.all().delete()
        for v in request.POST:
            if 'option' in v:
                selected_value=request.POST.get(v)
                spv=ServicePropertyValue.objects.get(pk=int(selected_value))
                sv=ServiceValue(service=service,servicepropertyvalue=spv)
                sv.save()
        service.price=request.POST.get('price')
        service.save()

    return render(request,'car_service/site_admin/servicevalue/update_form.html', {"service":service,'values':values })


