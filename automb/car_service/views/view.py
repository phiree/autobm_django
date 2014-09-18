from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
import datetime

from ..models import Tree, ServiceDetail, Supplier, Service,Bill
import jsonpickle
__author__ = 'Administrator'


def home(request):
    top_service_list = Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0], parent=None)
    return render(request, 'car_service/index.html', {'top_service_list': top_service_list})


# 服务列表
def service_list(request, service_type):
    top_service_list = Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0], parent=None)
    sl = Service.objects.all()
    if service_type != None:
        sl = sl.filter(service_type__id=service_type)
    service_ids = sl.values('id').distinct()
    supplier_list = Supplier.objects.filter(service__in=sl).distinct()

    return render(request, 'car_service/services.html',
                  {'service_type': service_type, 'supplier_list': supplier_list, 'top_service_list': top_service_list})

def supplier_list(request):
    area_list=Tree.objects.filter(tree_type=Tree.tree_type_choice[0][0], parent=None)
    supplier_list = Supplier.objects.all()
    top_service_list = Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0], parent=None)
    return render(request, 'car_service/suppliers.html',
                  {'supplier_list': supplier_list,'top_service_list': top_service_list})

# 服务详情
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
    service_detail=ServiceDetail.objects.get(pk=service_id)
    bill=Bill.objects.create(servicedetail=service_detail,order_date=datetime.datetime.now(),user=request.user,final_price=service_detail.price
    ,service_snapshot=str(service_detail)
    )
    bill.save()
    return redirect(reverse('car_service:front_web:bill_create_success'))