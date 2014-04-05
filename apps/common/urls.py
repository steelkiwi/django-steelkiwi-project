from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'common.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('profiles.urls', 'profiles')),
    url(r'^$', 'main', name='main'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
