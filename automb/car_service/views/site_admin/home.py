from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from ...decorators import group_required

# Create your views here.
@login_required
@group_required('administrators')
def index(request):
    #import pdb;pdb.set_trace()

    return render(request,'car_service/site_admin/index.html')
