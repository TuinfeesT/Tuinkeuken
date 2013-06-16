from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # TODO: how is recipe-details made referable from template as keuken:recipe-details?
    url(r'(?P<id>\d+)$', 'keuken.views.details', name='recipe'),
    url(r'(?P<author>\w+)$', 'keuken.views.list_by_author', name='recipes_by_author'),
)
