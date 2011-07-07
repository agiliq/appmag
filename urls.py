from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('browse.urls')),    
    url(r'^reviews/', include('blogango.urls')),
    url(r'^discuss/', include('dinette.urls')),
    url(r'^accounts/', include('socialauth.urls')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^search/', include('haystack.urls'),name='search'),
)
