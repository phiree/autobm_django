from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
import datetime

from ..models import   Supplier,  Bill


def my_home(request):
    return render(request, 'car_service/my/my_home.html')
def order_list(request):
    user=request.user
    orders=Bill.objects.filter(user=user)
    return render(request,'car_service/my/order_list.html',{'order_list':orders})

