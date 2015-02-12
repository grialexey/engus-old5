from django.conf.urls import patterns, url
from .views import ArticleDetailView, ArticleCreateView, ArticleUpdateView


urlpatterns = patterns('',
    url(r'^article-create/$', ArticleCreateView.as_view(), name='article-create'),
    url(r'^article-update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='article-update'),
    url(r'^(?P<category>[-_\w]+)/(?P<slug>[-_\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
)