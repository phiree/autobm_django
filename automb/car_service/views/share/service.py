from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from ...models import Supplier
from django.views.generic import ListView,CreateView,UpdateView,View
from django.core.urlresolvers import reverse
from ...forms import service_detail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your views here.
#字典管理

def index(request):
    return  render(request,'car_service/supplier_admin/home.html')




