from django.conf.urls import patterns, include, url
from .views import register, ProfileView, CardsGoalCreateView, CardsGoalDeleteView


urlpatterns = patterns('',
    url('^register/$', register, name='register'),
    url('^profile/$', ProfileView.as_view(), name='profile'),
    url('^goal/create/$', CardsGoalCreateView.as_view(), name='goal-create'),
    url('^goal/delete/(?P<pk>\d+)/$', CardsGoalDeleteView.as_view(), name='goal-delete'),
)
