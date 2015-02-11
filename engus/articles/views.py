# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):

    model = Article

    def get_queryset(self):
        articles = Article.objects.published()
        return articles


class ArticleDetailView(DetailView):

    context_object_name = 'article'
    model = Article

    def get_queryset(self):
        return Article.objects.published().filter(category__slug=self.kwargs['category'])
