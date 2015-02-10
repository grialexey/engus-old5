# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleDetailView(DetailView):

    context_object_name = 'article'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category'])
