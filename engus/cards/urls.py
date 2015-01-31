from django.conf.urls import patterns, url
from .views import DeckDetailView


urlpatterns = patterns('',
    url(r'^deck/(?P<slug>[-_\w]+)/$', DeckDetailView.as_view(), name='deck-detail'),
)