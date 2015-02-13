# -*- coding: utf-8 -*-
import json
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template import RequestContext, loader
from braces.views import LoginRequiredMixin
from .models import Card
from .forms import CardForm, DeleteCardForm, UpdateCardLevelForm


class MyCardListView(LoginRequiredMixin, ListView):

    paginate_by = 12

    def get_queryset(self):
        cards = Card.objects.filter(user=self.request.user).learning()
        if self.request.GET.get('sort') == 'repeat':
            cards = cards.order_by('next_repeat')
        return cards

    def get_template_names(self):
        return 'cards/card_list_my.html'

    def get_context_data(self, **kwargs):
        context = super(MyCardListView, self).get_context_data(**kwargs)
        context['mode'] = self.request.GET.get('mode', '')
        context['card_sorting'] = self.request.GET.get('sort')
        context['to_repeat_count'] = self.request.GET.get('filter')
        return context


@login_required
def create_card_view(request):
    if request.is_ajax() and request.method == 'POST':
        form = CardForm(request.POST, files=request.FILES)
        if form.is_valid():
            card_front_text = form.cleaned_data['front']
            card = form.save(commit=False)
            card.add_card_front(card_front_text, request.user)
            card.user = request.user
            card.save()
            card_template = loader.get_template('cards/card.html')
            context = RequestContext(request, {'card': card, })
            response_data = {
                'id': card.pk,
                'card': card_template.render(context),
                'cards_to_repeat_count': context['cards_to_repeat_count']
            }
            return HttpResponse(json.dumps(response_data), status=201, content_type="application/json")
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def update_card_view(request, pk):
    card_to_update = get_object_or_404(Card, pk=pk, user=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = CardForm(request.POST, instance=card_to_update)
        if form.is_valid():
            card_front_text = form.cleaned_data['front']
            card = form.save(commit=False)
            card.add_card_front(card_front_text, request.user)
            card.save()
            card_template = loader.get_template('cards/card.html')
            context = RequestContext(request, {'card': card, })
            response_data = {
                'id': card.pk,
                'card': card_template.render(context),
                'cards_to_repeat_count': context['cards_to_repeat_count']
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def update_card_level_view(request, pk):
    card_to_update = get_object_or_404(Card, pk=pk, user=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = UpdateCardLevelForm(request.POST, instance=card_to_update)
        if form.is_valid():
            form.update_level()
            card = form.save()
            card_template = loader.get_template('cards/card.html')
            context = RequestContext(request, {'card': card, })
            response_data = {
                'id': card.pk,
                'card': card_template.render(context),
                'cards_to_repeat_count': context['cards_to_repeat_count']
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def delete_card_view(request, pk):
    card_to_delete = get_object_or_404(Card, pk=pk, user=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = DeleteCardForm(request.POST, instance=card_to_delete)
        if form.is_valid():
            card_to_delete.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404
