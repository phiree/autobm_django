from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
admin.autodiscover()
import permission; permission.autodiscover()
urlpatterns = patterns(''
    # Examples:
    # url(r'^$', 'automb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ,url(r'^admin/', include(admin.site.urls))
    ,url(r'^profile/',include('userprofile.urls',namespace='userprofile'))
    ,url(r'^profile/change_password/$',views.password_change,  {'template_name':'reset_password.html'}, name='password_change'),
    url(r'^profile/change_password_done/$',views.password_change_done,  {'template_name':'password_change_successfully.html'},  name='password_change_done')
    ,url(r'',include('car_service.urls',namespace='car_service'))
    ,
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
