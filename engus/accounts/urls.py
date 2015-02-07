from django.conf.urls import patterns, include, url
from .views import register


urlpatterns = patterns('',
    url('^register/$', register, name='register'),
    url('^', include('django.contrib.auth.urls')),
)
