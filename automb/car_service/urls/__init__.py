from django.conf.urls import patterns,url,include

from car_service.views.site_admin import supplier, home, \
    carinfo, areainfo,servicetype,serviceproperty,\
    servicepropertyvalue,\
    service2 as site_admin_service2
from ..views import admin_supplier,view

from car_service.views.supplier_admin import service2 as supplier_admin_service2, home as supplier_admin_home

urlpatterns=patterns(''
                    #前台路由
                     ,url(r'', include('car_service.urls.front_web',namespace='front_web'))
                     #汽车管理
                    ,url(r'^site_admin/carinfo/list/$', carinfo.CarList.as_view( ),name='car_list' )

                    ,url(r'^site_admin/carinfo/create/$', carinfo.CarCreate.as_view( ),name='car_create' )
                     ,url(r'^site_admin/carinfo/update/(?P<id>\d+)/$', carinfo.CarUpdate.as_view( ),name='car_update' )#服务列表

                     #区域管理
                    ,url(r'^site_admin/areainfo/list/$', areainfo.AreaList.as_view( ),name='area_list' )
                    ,url(r'^site_admin/areainfo/create/$', areainfo.AreaCreate.as_view( ),name='area_create' )
                     ,url(r'^site_admin/areainfo/update/(?P<id>\d+)/$', areainfo.AreaUpdate.as_view( ),name='area_update' )
                     #服务列表
                    ,url(r'^site_admin/servicetype/list/$', servicetype.ServiceTypeList.as_view( ),name='servicetype_list' )
                    ,url(r'^site_admin/servicetype/create/$', servicetype.ServiceTypeCreate.as_view( ),name='servicetype_create' )
                     ,url(r'^site_admin/servicetype/update/(?P<id>\d+)/$', servicetype.ServiceTypeUpdate.as_view( ),name='servicetype_update' )
                    #服务属性
                     ,url(r'^site_admin/serviceproperty/list/$', serviceproperty.ServicePropertyList.as_view( ),name='serviceproperty_list' )
                    ,url(r'^site_admin/serviceproperty/create/$', serviceproperty.ServicePropertyCreate.as_view( ),name='serviceproperty_create' )
                     ,url(r'^site_admin/serviceproperty/update/(?P<id>\d+)/$', serviceproperty.ServicePropertyUpdate.as_view( ),name='serviceproperty_update' )


                   #服务属性值
                    ,url(r'^site_admin/servicepropertyvalue/list/$', servicepropertyvalue.ServicePropertyValueList.as_view( ),name='servicepropertyvalue_list' )
                    ,url(r'^site_admin/servicepropertyvalue/create/$', servicepropertyvalue.servicepropertyvalue_create,name='servicepropertyvalue_create' )
                     ,url(r'^site_admin/servicepropertyvalue/update/(?P<id>\d+)/$', servicepropertyvalue.servicepropertyvalue_update,name='servicepropertyvalue_update' )

                     #具体的服务定义
                     ,url(r'^site_admin/service2/list/$', site_admin_service2.ServiceList.as_view(),name='site_admin_service2_list' )
                    ,url(r'^site_admin/service2/create/$', site_admin_service2.ServiceCreate.as_view(),name='site_admin_service2_create' )
                     ,url(r'^site_admin/service2/update/(?P<id>\d+)/$', site_admin_service2.ServiceUpdate.as_view(),name='site_admin_service2_update' )
                     ,url(r'^site_admin/servicevalue/update/(?P<service_id>\d+)/$', site_admin_service2.update_value,name='site_admin_servicevalue_update' )

                    ,url(r'^site_admin/$', home.index,name='site_admin_index')

                    ,url(r'^site_admin/supplier(?:/list)?/$', supplier.SupplierList.as_view( ),name='supplier_list' )
                     ,url(r'^site_admin/supplier/create/$', supplier.SupplierCreate.as_view( ),name='supplier_create' )
                     ,url(r'^site_admin/supplier/update/(?P<id>\d+)/$', supplier.SupplierUpdate.as_view( ),name='supplier_update' )

                    ,url(r'^supplier_admin/$',admin_supplier.home,name='supplier_admin_home' )

                      ,url(r'^supplier_admin/service/list/$',supplier_admin_service2.ServiceList.as_view(),name='supplier_admin_service2_list' )
                    ,url(r'^supplier_admin/service/create/(?P<type_id>\d+)/$', supplier_admin_service2.create_service2,name='supplier_admin_service2_create' )
                     ,url(r'^supplier_admin/service/create/$', supplier_admin_service2.create_select_type,name='supplier_admin_service2_create_select_type' )
                     ,url(r'^supplier_admin/service/update/(?P<service_id>\d+)/$', supplier_admin_service2.edit_service2,name='supplier_admin_service2_update' )
                      #,url(r'^supplier_admin/service/disable/(?P<service_id>\d+)/$', supplier_admin_service2.disable_service2,name='supplier_admin_service2_disable' )
                     ,url(r'^supplier_admin/bill/list/$', admin_supplier.BillList.as_view(),name='supplier_admin_bill_list' )
                      ,url(r'^supplier_admin/bill/(?P<bill_id>\d+)/$', admin_supplier.BillDetail.as_view(),name='supplier_admin_bill_detail' )
                        ,url(r'^supplier_admin/bill/complete/(?P<bill_id>\d+)/$', admin_supplier.complete_bill,name='supplier_admin_complete_bill' )


                     ,url(r'^supplier_admin/supplier/list/$',supplier_admin_service2.SupplierList.as_view(),name='supplier_admin_supplier_list' )
                     ,url(r'^supplier_admin/supplier/create/$',supplier_admin_service2.SupplierCreate.as_view(),name='supplier_admin_supplier_create' )
                     ,url(r'^supplier_admin/supplier/update/(?P<supplier_id>\d+)/$',supplier_admin_service2.SupplierUpdate.as_view(),name='supplier_admin_supplier_update' )
                     ,url(r'^supplier_admin/supplier/create_success/(?P<supplier_id>\d+)/$', supplier_admin_service2.supplier_create_success, name='supplier_admin_supplier_create_success' )
                       ,url(r'^upload_file/$', view.upload_file, name='upload_file' )

                     )

                     