from django.conf.urls import patterns,url,include

from car_service.views.site_admin import supplier, home, \
    carinfo, areainfo,servicetype,serviceproperty,\
    servicepropertyvalue,\
    service2 as site_admin_service2
from car_service.views.supplier_admin import service2 as supplier_admin_service2

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


                      ,url(r'^supplier_admin/service/list/$',supplier_admin_service2.ServiceList.as_view(),name='supplier_admin_service2_list' )
                    ,url(r'^supplier_admin/service/create/$', supplier_admin_service2.ServiceCreate.as_view(),name='supplier_admin_service2_create' )
                     ,url(r'^supplier_admin/service/update/(?P<id>\d+)/$', supplier_admin_service2.ServiceUpdate.as_view(),name='supplier_admin_service2_update' )
                     ,url(r'^supplier_admin/servicevalue/update/(?P<service_id>\d+)/$', supplier_admin_service2.update_value,name='supplier_admin_servicevalue_update' )

                     )

                     