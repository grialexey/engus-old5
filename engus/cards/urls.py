from django.conf.urls import patterns, url
from .views import DeckDetailView, create_card_view, delete_card_view, MyCardListView


urlpatterns = patterns('',
    url(r'^deck/(?P<slug>[-_\w]+)/$', DeckDetailView.as_view(), name='deck-detail'),
    url(r'^create/$', create_card_view, name='card-create'),
    url(r'^delete/$', delete_card_view, name='card-delete'),
    url(r'^my/$', MyCardListView.as_view(), name='card-list-my'),
)