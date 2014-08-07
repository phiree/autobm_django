from django.shortcuts import render
from ..models import Tree
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse

# Create your views here.

class TreeList(ListView):
    model=Tree
    template_name = 'car_service/siteadmin/tree/tree_list.html'

    def get_queryset(self):
        cc=[]
        if len(self.kwargs)>0:
            cc=Tree.objects.filter(tree_type=self.kwargs['TreeType'])
        return cc


class TreeCreate(CreateView):
    model=Tree
    template_name = 'car_service/siteadmin/tree/tree_create_form.html'

    def get_success_url(self):
        treetype=self.kwargs['TreeType']
        return reverse('car_service:tree_update',args=(treetype, self.object.id,))


class TreeUpdate(UpdateView):
    model=Tree
    template_name = 'car_service/siteadmin/tree/tree_update_form.html'

    def get_object(self, queryset=None):
        obj = Tree.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:tree_update',args=(self.object.id,))


