# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()
admin.site.site_header = u'Администрирование Ингус.ру'


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^cards/', include('engus.cards.urls', namespace='cards')),
    url(r'^engusadmin/', include(admin.site.urls)),
    url(r'^accounts/', include('engus.accounts.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1],
                'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
            (r'^404/$', 'django.views.defaults.page_not_found'),
            (r'^500/$', 'django.views.defaults.server_error'),
            (r'^admin/', include(admin.site.urls)),
    )