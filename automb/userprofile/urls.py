from django.conf.urls import patterns,include,url
from django.contrib.auth import views
urlpatterns=patterns('',
                     url(r'^accounts/', include('django.contrib.auth.urls')),
                     url(r'^profile/$','userprofile.views.user_profile',name='user_profile'),


                     )