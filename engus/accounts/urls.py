from django.conf.urls import patterns, include, url
from .views import register, ProfileView


urlpatterns = patterns('',
    url('^register/$', register, name='register'),
    url('^profile/$', ProfileView.as_view(), name='profile'),
    url('^', include('django.contrib.auth.urls')),
)
