from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.template.response import TemplateResponse
from ..forms import fm_comment
from django.utils import timezone as datetime
from ..models import   Supplier,  Bill,ServiceType,Service2,UserComment
from ..biz import get_cookie,biz_search,service2
import jsonpickle
__author__ = 'Administrator'


def home(request):
    #top_service_list = Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0], parent=None)
    top_service_list=ServiceType.objects.filter(parent=None)
    return render(request, 'car_service/home.html', {'top_service_list': top_service_list})

def access_denied(request):
    return render(request,'car_service/access_denied.html')

def service_list_all(request):
    return service_list(request,None)
# 服务列表
def service_list(request, service_type_id):

    area_id=get_cookie.get_area(request)
    sl = Service2.objects.filter(supplier__area__id=area_id)

    if service_type_id != None:
        service_type=ServiceType.objects.get(pk=service_type_id)
        if service_type.parent!=None:
            sl = sl.filter(servicetype__id=service_type_id)
        else:
            sl=sl.filter(servicetype__parent__id=service_type_id)

    top_service_type_list=ServiceType.objects.filter(parent=None)

    return render(request, 'car_service/services.html',
                  { 'service_list': sl,'top_service_type_list':top_service_type_list,
                    'service_type_id':service_type_id})


def supplier_detail(request,supplier_id):
    supplier=Supplier.objects.get(pk=supplier_id)

    return render(request,'car_service/supplier.html', {'supplier':supplier})

def service_detail2_with_id(request,service_id):
    return  service_detail2(request,service_id,None,None)

def service_detail2_without_id(request,servicetype_id,supplier_id):
    return  service_detail2(request,None,servicetype_id,supplier_id)
# 服务详情
def service_detail2(request,service_id,servicetype_id,supplier_id):
    service=None
    if service_id!=None:
        service=Service2.objects.get(pk=service_id)
        supplier_id=service.supplier.id
        servicetype_id=service.servicetype.id

    services=Service2.objects.filter(supplier__id=supplier_id,servicetype__id=servicetype_id)

    if service==None:
        service=Service2.objects.filter(supplier__id=supplier_id,servicetype__id=servicetype_id)[0]
    comment_list=UserComment.objects.filter(bill__service__in=services)
    #todo 是否已经评论,是否已经购买 传递给template
    #有个问题 服务页面 servicedetail2.html 对应的是多个服务(不同条件组合对应不同服务, 需要使用ajax, 根据组合条件的变化判断用户是否已经评论过?)
    has_comment=False
    has_bought=False
    return render(request, 'car_service/servicedetail2.html',
                  {'merged_service':generate_service_detail(services),
                   'services':services,'service':service,
                   'paras':str(servicetype_id)+'_'+str(supplier_id),
                  'comment_list':comment_list
                  })
    pass
#ajax 判断用户是否已经评论过.
from django.template.loader import render_to_string
def comment_status(request):
    if request.method=='POST':
        service_id=int(request.POST.get('service_id'))
        result=service2.get_comment_status(request,service_id)
        fm=fm_comment.CommentForm()
        return TemplateResponse(request,'car_service/comment.html',
                                {'state':result['status'],'comment':result['comment'],
                                 'bill':result['bill'],
                                 'form':fm})
    elif request.is_ajax():
        pass
    else:
        pass
def comment_add(request,bill_id):
    fm=fm_comment.CommentForm(request.POST)
    instance=fm.instance
    instance.bill=Bill.objects.get(pk=bill_id)
    instance.user=request.user
    if fm.is_valid():
        fm.save()
    return render(request,'car_service/comment_successfully')

def supplier_list(request):

    supplier_list = Supplier.objects.all()


    return render(request, 'car_service/suppliers.html',
                  {'supplier_list': supplier_list})
#生成前台需要的数据
def generate_service_detail(services):
    '''
    期望的格式:
    results=[
        {'p':property,   #属性
        'v':[            #值
             {'vname':value,'services':[service1,service2]}, 值的名称 和 包含该值的 服务(选中该服务则)
             {'vname':value2,'services':[service1,service3]}
            ]
    ]
    '''
    results=[]

    properties=services[0].servicetype.serviceproperty_set.all()
    for p in properties:#every  properties
        result={}
        for s in services: #every services
            index=[pv.servicepropertyvalue.serviceproperty for pv in s.servicevalue_set.all()].index(p)#
            pv=s.servicevalue_set.all()[index].servicepropertyvalue#s 该属性的值
            if not any(k2['p']==p for k2 in results):#如果结果中还未添加该属性
                result['p']=p
                result['v_l']=[{'v':pv,'s':[s]}]#[pv]
                #result['s']=[s]
                results.append(result)
            else:
                index2=[k['p'] for k in results].index(p)
                result=results[index2]          #从结果列表中获取 该属性
                if any(pv==v for v in  [item['v'] for item in  result['v_l']]): # 该属性的值是否已经添加
                    index3=[item['v'] for item in  result['v_l']].index(pv)
                    results[index2]['v_l'][index3]['s'].append(s)
                else:
                    results[index2]['v_l'].append({'v':pv,'s':[s]})
    return results




def bill_create_success(request):
    return render(request,'car_service/bill_create_success.html')

@login_required
def bill_create(request,service_id):
    user=request.user
    #service_id=request.POST.get('service_id')
    service_detail=Service2.objects.get(pk=service_id)
    bill=Bill.objects.create(service=service_detail,order_date=datetime.now(),user=request.user,final_price=service_detail.price
    ,service_snapshot=str(service_detail)
    )
    bill.save()
    return redirect(reverse('car_service:front_web:bill_create_success'))

from ..forms.fm_register import RegisterForm
def user_register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'],
                                     password= form.cleaned_data['password'],
                                     email=form.cleaned_data['email'])
            return HttpResponseRedirect(redirect_to='/accounts/login')
    return render(request,'car_service/accounts/register.html',{'form':form})

def search(request):

    kw=request.GET.get('kw')
    search_result=biz_search.search(kw)
    return render(request,'car_service/search.html',{'kw':kw,'search_result':search_result})
    pass

import json
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
def upload_file(request):
    image=request.FILES.get('file')
    saved_path =default_storage.save(image.name,ContentFile(image.read()))

    data={'url':settings.MEDIA_URL+saved_path}
    return HttpResponse(json.dumps(data),content_type='application/json')
