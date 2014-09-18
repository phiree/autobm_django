from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse
from ...forms.fm_tree import TreeForm
from ...models import CarInfo
import jsonpickle
# Create your views here.

class CarList(ListView):
    model=CarInfo
    template_name = 'car_service/site_admin/carinfo/list.html'
    '''
    def get_queryset(self):
        cc=[]
        if len(self.kwargs)>0:
            cc=Tree.objects.filter(tree_type=self.kwargs['TreeType'])
        return cc
    '''

class CarCreate(CreateView):
    model=CarInfo
    template_name = 'car_service/site_admin/carinfo/car_update_form.html'
    def get_success_url(self):
        return reverse('car_service:car_update',args=(self.object.id,))



class CarUpdate(UpdateView):
    model=CarInfo
    template_name = 'car_service/site_admin/carinfo/car_update_form.html'
    #todo
    def get_object(self, queryset=None):
        obj = CarInfo.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
        return reverse('car_service:car_update',args=(self.object.id,))











