from django.conf.urls import patterns,url

from car_service.views.site_admin import supplier, home

from car_service.views import my, view

urlpatterns=patterns(''
                     ,url(r'^$', view.home,name='site_home')
                     ,url(r'^accounts/login.*','django.contrib.auth.views.login',{'template_name':'car_service/accounts/login.html'},name='login')
                     ,url(r'^accounts/logout.*','django.contrib.auth.views.logout',{'template_name':'car_service/accounts/logout.html'},name='logout')
                     ,url(r'^accounts/register.*',view.user_register,name='register')
                     #服务列表
                     ,url(r'^service_list/$', view.service_list_all,name='service_list')
                     ,url(r'^service_list/(?P<service_type_id>\d+)$', view.service_list,name='service_list')
                     ,url(r'^service/(?P<service_id>\d+)/$', view.service_detail2_with_id,name='service_detail_with_id')
                     ,url(r'^service/(?P<servicetype_id>\d+)/(?P<supplier_id>\d+)/$', view.service_detail2_without_id,name='service_detail_without_id')
                    #评论
                     ,url(r'^service/comment/status/$', view.comment_status,name='comment_status')
                     ,url(r'^service/comment/add/(?P<bill_id>\d+)$', view.comment_add,name='comment_add')
                     ,url(r'^service/comment/success$', view.comment_success,name='comment_success')
                     #商家列表
                     ,url(r'^supplier_list/$', view.supplier_list,name='supplier_list')
                     #跳转页面,写入cookies
                      ,url(r'^shr/(?P<supplier_id>\d+)/$', view.supplier_home_redirect,name='supplier_home_redirect')
                     ,url(r'^supplier/(?P<supplier_id>\d+)/$', view.supplier_detail,name='supplier_detail')
                      ,url(r'^supplier/(?P<supplier_id>\d+)/services$', view.supplier_detail,name='supplier_services')
                     #商家服务列表

                     #订单
                     ,url(r'^bill/create/(?P<service_id>\d+)$', view.bill_create,name='bill_create')
                     ,url(r'^bill/success_created/$', view.bill_create_success,name='bill_create_success')
                     #个人中心
                     ,url(r'^my$', my.my_home,name='my_home')
                     ,url(r'^my/orders$', my.order_list,name='my_orders')
                     ,url(r'^my/comment_list', my.comment_list_of_my,name='my_comment')
                     ,url(r'^my/my_promote', my.my_promote,name='my_promote')
                     ,url(r'^my/cars', my.cars,name='my_cars')

                     #权限错误
                     ,url(r'^access_denied/.*$', view.access_denied,name='access_denied')
                     #搜索
                     ,url(r'^search/$', view.search,name='search')
                     #推广链接跳转.
                     ,url(r'^pm_redt/', view.promote_redirect,name='promote_redirect')

                     #选择车类型
                     ,url(r'^car_typelist/', view.select_cartype,name='select_cartype')
                     #确认支付
                     ,url(r'^affirm_pay/', view.affirm_pay,name='affirm_pay')
                     #保养提醒
                     ,url(r'^upkeep_time/', view.upkeep_time,name='upkeep_time')
                     #商家详情
                     ,url(r'^shop_info/', view.shop_info,name='shop_info')

                     #优惠预约
                     ,url(r'^preferential_booking/', view.preferential_booking,name='preferential_booking')
                     #预约详情
                     ,url(r'^subscribe_info/', view.subscribe_info,name='subscribe_info')
                     #预约成功
                     ,url(r'^subscribe_success/', view.subscribe_success,name='subscribe_success')
                     ,url(r'^no_such_supplier/', view.no_such_supplier,name='no_such_supplier')

                     ,
                     )