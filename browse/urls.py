from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from appster.browse.views import *

urlpatterns = patterns('',
    url(r'^$', 'browse.views.index', name='index'),
    url(r'^browse/$', 'browse.views.home', name='home'),
    url(r'^category/(?P<slug>[^/]+)/$', 'browse.views.get_list_category', name='getcategory'),
)

