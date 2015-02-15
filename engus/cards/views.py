# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader
from django.utils import timezone
from braces.views import LoginRequiredMixin
from .models import Card
from .forms import CardForm, DeleteCardForm, UpdateCardLevelForm, CopyCardForm


class MyCardListView(LoginRequiredMixin, ListView):

    paginate_by = 12

    def get_queryset(self):
        cards = Card.objects.filter(user=self.request.user).learning()
        cards = cards.extra(select={'_is_to_repeat': "next_repeat > '%s'" % timezone.now()})
        cards = cards.order_by('_is_to_repeat', '-next_repeat')
        return cards

    def get_template_names(self):
        return 'cards/card_list_my.html'

    def get_context_data(self, **kwargs):
        context = super(MyCardListView, self).get_context_data(**kwargs)
        context['mode'] = self.request.GET.get('mode', '')
        context['is_repeat_mode'] = context['mode'] in ('repeat-left', 'repeat-right')
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
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        raise Http404


@login_required
def update_card_view(request, pk):
    card_to_update = get_object_or_404(Card, pk=pk, user=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = CardForm(request.POST, files=request.FILES, instance=card_to_update)
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
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse(form.errors, status=400)
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
            context = RequestContext(request, {'card': card, 'is_repeat_mode': True, })
            response_data = {
                'id': card.pk,
                'card': card_template.render(context),
                'cards_to_repeat_count': context['cards_to_repeat_count']
            }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        raise Http404


@login_required
def delete_card_view(request, pk):
    card_to_delete = get_object_or_404(Card, pk=pk, user=request.user)
    if request.is_ajax() and request.method == 'POST':
        form = DeleteCardForm(request.POST, instance=card_to_delete)
        if form.is_valid():
            card_to_delete.delete()
            response_data = {'cards_to_repeat_count': RequestContext(request)['cards_to_repeat_count'], }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        raise Http404


@login_required
def copy_card_view(request, pk):
    card = get_object_or_404(Card, pk=pk, article__isnull=False)
    if request.is_ajax() and request.method == 'POST':
        form = CopyCardForm(request.POST, instance=card)
        if form.is_valid():
            new_card = card.make_copy(request.user)
            new_card.save()
            response_data = {'cards_to_repeat_count': RequestContext(request)['cards_to_repeat_count'], }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        raise Http404
