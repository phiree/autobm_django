from django.conf.urls import patterns,url

from car_service.views.site_admin import supplier,tree, home,service as admin_service
from car_service.views.supplier_admin import service as supplier_service


urlpatterns=patterns(''

                     ,url(r'^site_admin/tree/list/(?P<TreeType>.+)/$', tree.TreeList.as_view( ),name='tree_list' )
                     ,url(r'^site_admin/tree/create/(?P<TreeType>.+)/$', tree.TreeCreate.as_view( ),name='tree_create' )
                     ,url(r'^site_admin/tree/update/(?P<TreeType>.+)/(?P<id>\d+)/$', tree.TreeUpdate.as_view( ),name='tree_update' )

                    ,url(r'^site_admin/supplier(?:/list)?/$', supplier.SupplierList.as_view( ),name='supplier_list' )
                     ,url(r'^site_admin/supplier/create/$', supplier.SupplierCreate.as_view( ),name='supplier_create' )
                     ,url(r'^site_admin/supplier/update/(?P<id>\d+)/$', supplier.SupplierUpdate.as_view( ),name='supplier_update' )

                    ,url(r'^site_admin/service(?:/list)?/$', admin_service.ServiceList.as_view( ),name='service_list' )
                     ,url(r'^site_admin/service/create/$', admin_service.service_create,name='service_create' )
                     ,url(r'^site_admin/service/update/(?P<id>\d+)/$', admin_service.service_update,name='service_update' )

                     ,url(r'^supplier_admin/$', supplier_service.index,name='supplier_admin_index' )
                    ,url(r'^supplier_admin/service(?:/list)?/$', supplier_service.service_list,name='supplier_admin_service_list' )
                    ,url(r'^supplier_admin/service/create/$', supplier_service.create,name='supplier_admin_service_create' )
                    ,url(r'^supplier_admin/service/update/(?P<id>\d+)/$', supplier_service.update,name='supplier_admin_service_update' )
                     ,url(r'^site_admin/$', home.index,name='site_admin_index'),

                     )

                     