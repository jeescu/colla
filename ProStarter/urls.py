from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'appstarter.controller.welcome.welcome', name='private'),
    url(r'^colla/', include('appstarter.urls', namespace="colla")),
    url(r'^admin/', include(admin.site.urls)),
)
