from django.conf.urls import patterns,url
from car_service.views import supplier,tree,service,home

urlpatterns=patterns(''
                     #,url(r'^siteadmin/tree/list/$', views_tree.TreeList.as_view( ),name='tree_list' )
                     ,url(r'^site_admin/tree/list/(?P<TreeType>.+)/$', tree.TreeList.as_view( ),name='tree_list' )
                     ,url(r'^site_admin/tree/create/(?P<TreeType>.+)/$', tree.TreeCreate.as_view( ),name='tree_create' )
                     ,url(r'^site_admin/tree/update/(?P<TreeType>.+)/(?P<id>\d+)/$', tree.TreeUpdate.as_view( ),name='tree_update' )

                    ,url(r'^site_admin/supplier(?:/list)?/$', supplier.SupplierList.as_view( ),name='supplier_list' )
                     ,url(r'^site_admin/supplier/create/$', supplier.SupplierCreate.as_view( ),name='supplier_create' )
                     ,url(r'^site_admin/supplier/update/(?P<id>\d+)/$', supplier.SupplierUpdate.as_view( ),name='supplier_update' )

                    ,url(r'^site_admin/service(?:/list)?/$', service.ServiceList.as_view( ),name='service_list' )
                     ,url(r'^site_admin/service/create/$', service.service_create,name='service_create' )
                     ,url(r'^site_admin/service/update/(?P<id>\d+)/$', service.service_update,name='service_update' )

                     ,url(r'^site_admin/$', home.index,name='site_admin_index'),

                     )

                     