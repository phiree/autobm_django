from django.conf.urls import patterns,url

from car_service.views.site_admin import supplier,tree, home,service as admin_service
from car_service.views.supplier_admin import service as supplier_service
from car_service.views import my, view

urlpatterns=patterns(''
                     ,url(r'^$', view.home,name='site_home')
                     ,url(r'^accounts/login.*','django.contrib.auth.views.login',{'template_name':'car_service/accounts/login.html'},name='login')
                     ,url(r'^accounts/logout.*','django.contrib.auth.views.logout',{'template_name':'car_service/accounts/logout.html'},name='logout')
                     #服务列表
                     ,url(r'^service_list/(?P<service_type>\d+)$', view.service_list,name='service_list')
                     ,url(r'^service/(?P<service_id>\d+)/(?:(?P<detail_id>\d+))?$', view.service_detail,name='service_detail')
                     #商家列表
                     ,url(r'^supplier_list/$', view.supplier_list,name='supplier_list')
                     #订单
                     ,url(r'^bill/create/(?P<service_id>\d+)$', view.bill_create,name='bill_create')
                     ,url(r'^bill/success_created/$', view.bill_create_success,name='bill_create_success')
                     #个人中心
                     ,url(r'^my$', my.my_home,name='my_home')
                     )