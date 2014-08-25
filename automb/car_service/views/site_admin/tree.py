from django.shortcuts import get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse
from ...forms.fm_tree import TreeForm
from ...models import Tree
import jsonpickle
# Create your views here.

class TreeList(ListView):
    model=Tree
    template_name = 'car_service/site_admin/tree/tree_list.html'
    '''
    def get_queryset(self):
        cc=[]
        if len(self.kwargs)>0:
            cc=Tree.objects.filter(tree_type=self.kwargs['TreeType'])
        return cc
    '''

class TreeCreate(CreateView):
    form_class=TreeForm
    #model=Tree
    template_name = 'car_service/site_admin/tree/tree_update_form.html'
    def get_initial(self):

        initial = super(TreeCreate, self).get_initial()
        tree_type=self.kwargs.get('TreeType')
        tree=Tree()
        tree.tree_type=tree_type
        initial['slug']=tree
        return {'initial':tree }

    def get_success_url(self):
        treetype=self.kwargs['TreeType']
        return reverse('car_service:tree_update',args=(treetype, self.object.id,))


class TreeUpdate(UpdateView):
    model=Tree
    template_name = 'car_service/site_admin/tree/tree_update_form.html'

    def get_object(self, queryset=None):
        obj = Tree.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self):
         return reverse('car_service:tree_update',args=(self.kwargs['TreeType'],self.object.id,))

def create_car_tree_js(request):
    '''生成车型js,供前台选择'''
    car_factories=Tree.objects.filter(tree_type=Tree.tree_type_choice[1][0],parent=None)




