from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse

from ...models import AreaInfo
import jsonpickle
# Create your views here.
#todo 使用内联表单 一次性创建多个子内容.
class AreaList(ListView):
    model=AreaInfo
    template_name = 'car_service/site_admin/areainfo/list.html'


class AreaCreate(CreateView):
    model=AreaInfo
    template_name = 'car_service/site_admin/areainfo/update_form.html'
    def get_success_url(self):
        return reverse('car_service:area_update',args=(self.object.id,))



class AreaUpdate(UpdateView):
    model=AreaInfo
    template_name = 'car_service/site_admin/areainfo/update_form.html'
    #todo 
    def get_object(self, queryset=None):
        obj = AreaInfo.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:area_update',args=(self.object.id,))











