from django.conf.urls import patterns,url,include

from car_service.views.site_admin import supplier,tree, home,service as admin_service, \
    carinfo, areainfo,servicetype,serviceproperty,service2\
    ,servicepropertyvalue,servicevalue

from car_service.views.supplier_admin import service as supplier_service
from car_service.views import view

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
                    ,url(r'^site_admin/servicepropertyvalue/create/$', servicepropertyvalue.ServicePropertyValueCreate.as_view( ),name='servicepropertyvalue_create' )
                     ,url(r'^site_admin/servicepropertyvalue/update/(?P<id>\d+)/$', servicepropertyvalue.ServicePropertyValueUpdate.as_view( ),name='servicepropertyvalue_update' )

                     #具体的服务定义
                     ,url(r'^site_admin/service2/list/$', service2.ServiceList.as_view(),name='site_admin_service2_list' )
                    ,url(r'^site_admin/service2/create/$', service2.ServiceCreate.as_view(),name='site_admin_service2_create' )
                     ,url(r'^site_admin/service2/update/(?P<id>\d+)/$', service2.ServiceUpdate.as_view(),name='site_admin_service2_update' )
                     ,url(r'^site_admin/servicevalue/update/(?P<service_id>\d+)/$', servicevalue.update_value,name='site_admin_servicevalue_update' )

                    ,url(r'^site_admin/$', home.index,name='site_admin_index')
                     ,url(r'^site_admin/tree/list/(?P<TreeType>.+)/$', tree.TreeList.as_view( ),name='tree_list' )
                     ,url(r'^site_admin/tree/create/(?P<TreeType>.+)/$', tree.TreeCreate.as_view(),name='tree_create' )
                     ,url(r'^site_admin/tree/update/(?P<TreeType>.+)/(?P<id>\d+)/$', tree.TreeUpdate.as_view( ),name='tree_update' )
                    # ,url(r'^site_admin/area/generate/$', tree.generate_area_list,name='generate_area_list' )

                    ,url(r'^site_admin/supplier(?:/list)?/$', supplier.SupplierList.as_view( ),name='supplier_list' )
                     ,url(r'^site_admin/supplier/create/$', supplier.SupplierCreate.as_view( ),name='supplier_create' )
                     ,url(r'^site_admin/supplier/update/(?P<id>\d+)/$', supplier.SupplierUpdate.as_view( ),name='supplier_update' )

                    ,url(r'^site_admin/service(?:/list)?/$', admin_service.ServiceList.as_view( ),name='site_admin_service_list' )
                    ,url(r'^site_admin/service/edit(?:/(?P<id>\d+))?/$', admin_service.edit,name='site_admin_service_edit' )

                     ,url(r'^supplier_admin/$', supplier_service.index,name='supplier_admin_index' )
                     ,url(r'^supplier_admin/service(?:/list)?/$', supplier_service.service_list,name='supplier_admin_service_list' )
                     ,url(r'^supplier_admin/service/edit(?:/(?P<id>\d+))?/$', supplier_service.edit,name='supplier_admin_service_edit' )

                     )

                     