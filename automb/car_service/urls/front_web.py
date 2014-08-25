from django.conf.urls import patterns,url

from car_service.views.site_admin import supplier,tree, home,service as admin_service
from car_service.views.supplier_admin import service as supplier_service
from car_service.views import view

urlpatterns=patterns(''
                     ,url(r'^$', view.home,name='site_home')
                     #服务列表
                     ,url(r'^service_list/(?P<service_type>\d+)$', view.service_list,name='service_list')
                     ,url(r'^service/(?P<service_id>\d+)/(?:(?P<detail_id>\d+))?$', view.service_detail,name='service_detail')
                     )

                     