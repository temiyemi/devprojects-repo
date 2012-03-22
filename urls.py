from settings import DEBUG
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    #url(r'^$', 'devprojects.views.home', name='home'),
    url(r'^ims/', include('devprojects.ims.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

)
#urlpatterns += staticfiles_urlpatterns()
if DEBUG:
    urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
            {'document_root': 'static'}
        ))