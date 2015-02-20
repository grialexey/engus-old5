from django.conf.urls import patterns, include, url
from .views import (register, ProfileView, CardsGoalCreateView, CardsGoalDeleteView, CardsGoalUpdateView,
                    CardsGoalDetailView)


urlpatterns = patterns('',
    url('^register/$', register, name='register'),
    url('^profile/$', ProfileView.as_view(), name='profile'),
    url('^goal/(?P<pk>\d+)/$', CardsGoalDetailView.as_view(), name='goal-detail'),
    url('^goal/create/$', CardsGoalCreateView.as_view(), name='goal-create'),
    url('^goal/update/(?P<pk>\d+)/$', CardsGoalUpdateView.as_view(), name='goal-update'),
    url('^goal/delete/(?P<pk>\d+)/$', CardsGoalDeleteView.as_view(), name='goal-delete'),
)
