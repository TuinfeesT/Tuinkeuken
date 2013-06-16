from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tuinkeuken.views.index', name='index'),
    url(r'^recipes/', include('keuken.urls', namespace='keuken')),

    url(r'^admin/', include(admin.site.urls)),
)
