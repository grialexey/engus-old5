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


def get_cards_counts_for_user(user):
    return {
        'to_learn_cards_count': Card.objects.to_learn_for_user(user=user).count(),
        'to_repeat_cards_count': Card.objects.to_repeat_for_user(user=user).count(),
        'learned_cards_count': Card.objects.learned_for_user(user=user).count(),
    }


class MyCardListView(LoginRequiredMixin, ListView):

    paginate_by = 12

    def get_queryset(self):
        cards_filter = self.request.GET.get('filter')
        if cards_filter == 'new':
            cards = Card.objects.new_for_user(user=self.request.user)
        elif cards_filter == 'in-learning':
            cards = Card.objects.in_learning_for_user(user=self.request.user)
        elif cards_filter == 'to-repeat':
            cards = Card.objects.to_repeat_for_user(user=self.request.user)
        elif cards_filter == 'learned':
            cards = Card.objects.learned_for_user(user=self.request.user)
        else:
            cards = Card.objects.to_learn_for_user(user=self.request.user)
        return cards

    def get_template_names(self):
        if self.request.is_ajax():
            return 'cards/card_list_my_ajax.html'
        else:
            return 'cards/card_list_my.html'

    def get_context_data(self, **kwargs):
        context = super(MyCardListView, self).get_context_data(**kwargs)
        context['mode'] = self.request.GET.get('mode', '')
        context['cards_filter'] = self.request.GET.get('filter')
        context['cards_counts'] = get_cards_counts_for_user(self.request.user)
        return context


@login_required
def create_card_view(request):
    if request.is_ajax() and request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card_front_text = form.cleaned_data['front']
            card = form.save(commit=False)
            card.learner = request.user
            card.add_card_front(card_front_text, request.user)
            card.save()
            return HttpResponse(status=201)
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def update_card_view(request, pk):
    card_to_update = get_object_or_404(Card, pk=pk, learner=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = CardForm(request.POST, instance=card_to_update)
        if form.is_valid():
            card_front_text = form.cleaned_data['front']
            card = form.save(commit=False)
            card.add_card_front(card_front_text, request.user)
            card.save()
            card_template = loader.get_template('cards/card.html')
            response_data = {
                'card': card_template.render(RequestContext(request, {'card': card, })),
                'cards_counts': get_cards_counts_for_user(request.user)
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def update_card_level_view(request, pk):
    card_to_update = get_object_or_404(Card, pk=pk, learner=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = UpdateCardLevelForm(request.POST, instance=card_to_update)
        if form.is_valid():
            form.update_level()
            card = form.save()
            card_template = loader.get_template('cards/card.html')
            response_data = {
                'card': card_template.render(RequestContext(request, {'card': card, })),
                'cards_counts': get_cards_counts_for_user(request.user)
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def delete_card_view(request, pk):
    card_to_delete = get_object_or_404(Card, pk=pk, learner=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = DeleteCardForm(request.POST, instance=card_to_delete)
        if form.is_valid():
            card_to_delete.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404
