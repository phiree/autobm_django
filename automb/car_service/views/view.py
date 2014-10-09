from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect

from django.utils import timezone as datetime
from ..models import Tree, ServiceDetail, Supplier, Service,Bill,ServiceType,Service2
import jsonpickle
__author__ = 'Administrator'


def home(request):
    top_service_list = Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0], parent=None)
    #top_service_list=ServiceType.objects.filter(parent=None)
    return render(request, 'car_service/index.html', {'top_service_list': top_service_list})


# 服务列表
def service_list(request, service_type):

    sl = Service2.objects.all()
    if service_type != None:
        sl = sl.filter(servicetype__id=service_type)

    supplier_list = Supplier.objects.filter(service2__in=sl).distinct()

    return render(request, 'car_service/services.html',
                  {'service_type': service_type, 'supplier_list': supplier_list,})

def supplier_list(request):
    area_list=Tree.objects.filter(tree_type=Tree.tree_type_choice[0][0], parent=None)
    supplier_list = Supplier.objects.all()
    top_service_list = Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0], parent=None)

    return render(request, 'car_service/suppliers.html',
                  {'supplier_list': supplier_list,'top_service_list': top_service_list})
def service_detail2_with_id(request,service_id):
    return  service_detail2(request,service_id,None,None)

def service_detail2_without_id(request,servicetype_id,supplier_id):
    return  service_detail2(request,None,servicetype_id,supplier_id)
# 服务详情
def service_detail2(request,service_id,servicetype_id,supplier_id):
    services=[]
    service=None
    if service_id!=None:
        service=Service2.objects.get(pk=service_id)
        supplier_id=service.supplier.id
        servicetype_id=service.servicetype.id

    services=Service2.objects.filter(supplier__id=supplier_id,servicetype__id=servicetype_id)
    if service==None:
        service=Service2.objects.filter(supplier__id=supplier_id,servicetype__id=servicetype_id)[0]



    return render(request, 'car_service/servicedetail2.html', {'merged_service':generat_service_detail(services), 'services':services,'service':service,'paras':str(servicetype_id)+'_'+str(supplier_id)})
    pass
#生成前台需要的数据
def generat_service_detail(services):

    results=[]
    '''
    results=[
        {'p':property,
        'v':[
             {'vname':value,'services':[service1,service2]},
             {'vname':value2,'services':[service1,service3]}
            ]
    ]
    '''
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





def service_detail(request, service_id, detail_id):

    service = Service.objects.get(pk=service_id)
    only_one=True if service.servicedetail_set.all().count()==1 else False
    detail=None;
    json_detail_list=serializers.serialize("json", service.servicedetail_set.all(),use_natural_keys=True)
    cc= jsonpickle.encode(service.servicedetail_set.all())
    #aa=serializers.serialize("json", list(service.servicedetail_set.all())[0])
    if detail_id != None:
        detail = ServiceDetail.objects.get(pk=detail_id)


    properties = service.servicedetail_set.values_list()

    brand_ids = [a[2] for a in properties]
    brand_list = Tree.objects.filter(id__in=brand_ids)

    wash_type_ids = [a[3] for a in properties]
    wash_type_list = Tree.objects.filter(id__in=wash_type_ids)

    sound_proofing_type_ids = [a[4] for a in properties]
    sound_proofing_type_list = Tree.objects.filter(id__in=sound_proofing_type_ids)

    foil_type_ids = [a[5] for a in properties]
    foil_type_list = Tree.objects.filter(id__in=foil_type_ids)

    foil_model_front_ids = [a[6] for a in properties]
    foil_model_front_list = Tree.objects.filter(id__in=foil_model_front_ids)

    foil_model_sides_back_ids = [a[7] for a in properties]
    foil_model_sides_back_list = Tree.objects.filter(id__in=foil_model_sides_back_ids)

    glass_damage_size_ids = [a[8] for a in properties]
    glass_damage_size_list = Tree.objects.filter(id__in=glass_damage_size_ids)

    tire_repair_type_ids = [a[9] for a in properties]
    tire_repair_type_list = Tree.objects.filter(id__in=tire_repair_type_ids)

    body_damage_size_ids = [a[10] for a in properties]
    body_damage_size_list = Tree.objects.filter(id__in=body_damage_size_ids)

    sound_suit_ids = [a[11] for a in properties]
    sound_suit_list = Tree.objects.filter(id__in=sound_suit_ids)

    main_light_suit_ids = [a[12] for a in properties]
    main_light_suit_list = Tree.objects.filter(id__in=main_light_suit_ids)
    detail_json=serializers.serialize('json',service.servicedetail_set.all())
    return render(request, 'car_service/servicedetail2.html', {'service': service,'only_one':only_one,
                                                               'detail':detail,
                                                              'brand_list': brand_list

        , 'wash_type_list': wash_type_list
        , 'selected_sound_proofing_type_list': sound_proofing_type_list
        , 'foil_type_list': foil_type_list
        , 'foil_model_front_list': foil_model_front_list
        , 'foil_model_sides_back_list': foil_model_sides_back_list
        , 'glass_damage_size_list': glass_damage_size_list
        , 'tire_repair_type_list': tire_repair_type_list
        , 'body_damage_size_list': body_damage_size_list
        , 'sound_suit_list': sound_suit_list
        , 'main_light_suit_list': main_light_suit_list

        ,'json_detail_list':json_detail_list
    })

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