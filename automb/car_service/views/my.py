from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
import datetime

from ..models import Tree, ServiceDetail, Supplier, Service,Bill


def my_home(request):
    return render(request, 'car_service/my/my_home.html')

