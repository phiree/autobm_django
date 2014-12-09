from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from ..models import UserComment
import datetime

from ..models import   Supplier,  Bill


def my_home(request):
    return render(request, 'car_service/my/my_home.html')
def order_list(request):
    user=request.user
    orders=Bill.objects.filter(user=user)
    return render(request,'car_service/my/order_list.html',{'order_list':orders})

def comment_list_of_my(request):
    return comment_list(request,None,user_id=request.user.id,template='car_service/my/comment_list.html')


def comment_list(request,bill_id,user_id,template):
    if bill_id:
        comment_list=UserComment.objects.filter(bill__id=bill_id)
    elif user_id:
        comment_list=UserComment.objects.filter(bill__user__id=user_id)
    return render(request,template,{'comment_list':comment_list})

