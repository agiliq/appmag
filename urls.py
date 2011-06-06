from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'browse.views.index'),
    url(r'^', include('browse.urls')),
        # url(r'^appster/', include('appster.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^forum/',include(dinette.urls)),
	(r'^blog/', include('blogango.urls')),
    (r'^forum/', include('dinette.urls')),
    (r'^accounts/', include('socialauth.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
