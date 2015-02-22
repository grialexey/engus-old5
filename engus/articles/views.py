# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import JsonResponse, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin
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

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['page_title'] = self.object.name
        return context


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
        return reverse('accounts:profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleUpdateView, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(ArticleUpdateView, self).get_queryset()
        return base_qs.filter(author=self.request.user)


@login_required
def copy_article_cards_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        for card in article.card_set.public():
            new_card = card.make_copy(request.user)
            new_card.save()
        response_data = {'cards_to_repeat_count': RequestContext(request)['cards_to_repeat_count'], }
        return JsonResponse(response_data)
    else:
        raise Http404

