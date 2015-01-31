from django.conf.urls import patterns, url
from .views import DeckDetailView, create_new_card_ajax_view, MyCardListView


urlpatterns = patterns('',
    url(r'^deck/(?P<slug>[-_\w]+)/$', DeckDetailView.as_view(), name='deck-detail'),
    url(r'^card-create-ajax/$', create_new_card_ajax_view, name='card-create-ajax'),
    url(r'^my/$', MyCardListView.as_view(), name='my-card-list'),
)