from django.conf.urls import patterns,url,include

from car_service.views.site_admin import supplier,tree, home,service as admin_service
from car_service.views.supplier_admin import service as supplier_service
from car_service.views import view

urlpatterns=patterns(''
                    #前台路由
                     ,url(r'', include('car_service.urls.front_web',namespace='front_web'))
                     #服务列表

                    ,url(r'^site_admin/$', home.index,name='site_admin_index')
                     ,url(r'^site_admin/tree/list/(?P<TreeType>.+)/$', tree.TreeList.as_view( ),name='tree_list' )
                     ,url(r'^site_admin/tree/create/(?P<TreeType>.+)/$', tree.TreeCreate.as_view(),name='tree_create' )
                     ,url(r'^site_admin/tree/update/(?P<TreeType>.+)/(?P<id>\d+)/$', tree.TreeUpdate.as_view( ),name='tree_update' )

                    ,url(r'^site_admin/supplier(?:/list)?/$', supplier.SupplierList.as_view( ),name='supplier_list' )
                     ,url(r'^site_admin/supplier/create/$', supplier.SupplierCreate.as_view( ),name='supplier_create' )
                     ,url(r'^site_admin/supplier/update/(?P<id>\d+)/$', supplier.SupplierUpdate.as_view( ),name='supplier_update' )

                    ,url(r'^site_admin/service(?:/list)?/$', admin_service.ServiceList.as_view( ),name='site_admin_service_list' )
                     ,url(r'^site_admin/service/edit(?:/(?P<id>\d+))?/$', admin_service.edit,name='site_admin_service_edit' )

                     ,url(r'^supplier_admin/$', supplier_service.index,name='supplier_admin_index' )
                     ,url(r'^supplier_admin/service(?:/list)?/$', supplier_service.service_list,name='supplier_admin_service_list' )
                     ,url(r'^supplier_admin/service/edit(?:/(?P<id>\d+))?/$', supplier_service.edit,name='supplier_admin_service_edit' )
                     )

                     