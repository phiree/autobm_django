from django.shortcuts import render

__author__ = 'Administrator'

def home(request):
    return render(request,'car_service/supplier_admin/home.html')