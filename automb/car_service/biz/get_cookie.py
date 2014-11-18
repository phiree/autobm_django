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
def get_area(request):
    return request.COOKIES.get('area_id')







