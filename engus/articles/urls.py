from django.conf.urls import patterns, url
from .views import ArticleDetailView


urlpatterns = patterns('',
    url(r'^(?P<slug>[-_\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
)