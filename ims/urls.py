from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='home_url'),

    url(r'^partners$', partners, name='partners_url'),
    url(r'^partner/(?P<id>\d+)$', partner, name='partner_url'),

    url(r'^projects$', projects, name='projects_url'),
    url(r'^project/(?P<id>\d+)$', project, name='project_url'),

    url(r'^recipients$', recipients, name='recipients_url'),
    url(r'^recipient/(?P<id>\d+)$', recipient, name='recipient_url'),

    #search url
)