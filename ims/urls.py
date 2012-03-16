from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', index),

    url(r'^partners$', partners),
    url(r'^partner/(?P<id>\d+)$', partner),

    url(r'^projects$', projects),
    url(r'^project/(?P<id>\d+)$', project),

    url(r'^recipients$', recipients),
    url(r'^recipient/(?P<id>\d+)$', recipient),

    #search url

)