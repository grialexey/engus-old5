from django.conf.urls import patterns, url
from .views import ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleListView, copy_article_cards_view


urlpatterns = patterns('',
    url(r'^article-create/$', ArticleCreateView.as_view(), name='article-create'),
    url(r'^article-update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='article-update'),
    url(r'^(?P<category>[-_\w]+)/$', ArticleListView.as_view(), name='article-list'),
    url(r'^(?P<category>[-_\w]+)/(?P<slug>[-_\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^api/article/(?P<pk>\d+)/copy-cards/$', copy_article_cards_view, name='api-copy-article-cards'),
)