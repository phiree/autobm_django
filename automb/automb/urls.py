from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(''
    # Examples:
    # url(r'^$', 'automb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ,url(r'^accounts/login.+','django.contrib.auth.views.login',{'template_name':'car_service/login.html'},)
    ,url(r'^accounts/logout.+','django.contrib.auth.views.logout',{'template_name':'car_service /login.html'}, )
    ,url(r'^car_service/',include('car_service.urls',namespace='car_service'))
    ,url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
