from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from browse.views import *

urlpatterns = patterns('',
    url(r'^$', 'browse.views.index', name='index'),
    url(r'^browse/$', 'browse.views.home', name='home'),
    url(r'^device/$', 'browse.views.device', name='device'),
    url(r'^developer/$', 'browse.views.developer', name='developer'),
    url(r'^platform/$', 'browse.views.platform', name='platform'),
    url(r'^category/(?P<slug>[^/]+)/$', 'browse.views.get_list_category', name='getcategory'),
    url(r'^app/(?P<id>[^/]+)/$', 'browse.views.get_app', name='getapplication'),
    url(r'^device/(?P<slug>[^/]+)/$', 'browse.views.get_list_device', name='getdevice'),
    url(r'^developer/(?P<slug>[^/]+)/$', 'browse.views.get_list_developer', name='getdeveloper'),
    url(r'^platform/(?P<slug>[^/]+)/$', 'browse.views.get_list_platform', name='getplatform'),
)

