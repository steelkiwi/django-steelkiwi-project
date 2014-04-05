from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'common.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('profiles.urls', 'profiles')),
    url(r'^$', 'main', name='main'),
)
