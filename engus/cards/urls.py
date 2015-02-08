from django.conf.urls import patterns, url
from .views import (DeckDetailView, create_card_view, delete_card_view, update_card_view, MyCardListView,
                    update_card_level_view)


urlpatterns = patterns('',
    url(r'^deck/(?P<slug>[-_\w]+)/$', DeckDetailView.as_view(), name='deck-detail'),
    url(r'^create/$', create_card_view, name='card-create'),
    url(r'^delete/$', delete_card_view, name='card-delete'),
    url(r'^update/$', update_card_view, name='card-update'),
    url(r'^update-level/$', update_card_level_view, name='card-update-level'),
    url(r'^my/$', MyCardListView.as_view(), name='card-list-my'),
)