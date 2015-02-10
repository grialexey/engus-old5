from django.conf.urls import patterns, url
from .views import create_card_view, delete_card_view, update_card_view, MyCardListView, update_card_level_view


urlpatterns = patterns('',
    url(r'^my/$', MyCardListView.as_view(), name='card-list-my'),
    url(r'^api/card/create/$', create_card_view, name='card-create'),
    url(r'^api/card/delete/(?P<pk>\d+)/$', delete_card_view, name='card-delete'),
    url(r'^api/card/update/(?P<pk>\d+)/$', update_card_view, name='card-update'),
    url(r'^api/card/update-level/(?P<pk>\d+)/$', update_card_level_view, name='card-update-level'),
)