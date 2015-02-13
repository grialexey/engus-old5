# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, PermissionRequiredMixin
from .forms import ArticleCreateForm, ArticleUpdateForm
from .models import Article


class ArticleListView(ListView):

    model = Article

    def get_queryset(self):
        articles = Article.objects.published()
        if self.kwargs.get('category'):
            articles = articles.filter(category__slug=self.kwargs['category'])
        return articles


class ArticleDetailView(DetailView):

    context_object_name = 'article'
    model = Article

    def get_queryset(self):
        return Article.objects.published().filter(category__slug=self.kwargs['category'])


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_create.html'

    def get_success_url(self):
        return reverse('articles:article-update', kwargs={'pk': self.object.pk, })

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):

    model = Article
    form_class = ArticleUpdateForm
    template_name = 'articles/article_update.html'

    def get_success_url(self):
        return reverse('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleUpdateView, self).form_valid(form)
