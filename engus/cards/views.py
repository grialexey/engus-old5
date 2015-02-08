# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from braces.views import LoginRequiredMixin
from .models import Deck, Card, CardFront
from .forms import CreateCardForm, DeleteCardForm, UpdateCardForm, UpdateCardLevelForm


class DeckDetailView(DetailView):

    context_object_name = 'deck'
    model = Deck


class MyCardListView(LoginRequiredMixin, ListView):

    paginate_by = 12

    def get_queryset(self):
        return Card.objects.filter(learner=self.request.user)

    def get_template_names(self):
        if self.request.is_ajax():
            return 'cards/card_list_my_ajax.html'
        else:
            return 'cards/card_list_my.html'


@login_required
def create_card_view(request):
    if request.is_ajax() and request.method == 'POST':
        form = CreateCardForm(request.POST)
        if form.is_valid():
            card_front = form.cleaned_data.get('front').strip()
            card_back = form.cleaned_data.get('back', '').strip()
            card_example = form.cleaned_data.get('example', '').strip()
            try:
                card_front_obj = CardFront.objects.get(text__iexact=card_front, is_public=True)
            except CardFront.DoesNotExist:
                card_front_obj = CardFront(text=card_front, author=request.user)
                card_front_obj.save()
            Card.objects.create(front=card_front_obj, back=card_back, example=card_example, learner=request.user)
            return HttpResponse(status=201)
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def update_card_view(request):
    if request.is_ajax() and request.method == 'POST':
        form = UpdateCardForm(request.POST)
        if form.is_valid():
            pk = form.cleaned_data.get('pk')
            front = form.cleaned_data.get('front').strip()
            back = form.cleaned_data.get('back', '').strip()
            example = form.cleaned_data.get('example', '').strip()
            try:
                card_obj = Card.objects.get(pk=pk, learner=request.user)
            except Card.DoesNotExist:
                return HttpResponseBadRequest()
            if front != card_obj.front.text:
                # if not card_obj.front.is_public:
                #     card_obj.delete()
                try:
                    card_front_obj = CardFront.objects.get(text__iexact=front, is_public=True)
                except CardFront.DoesNotExist:
                    card_front_obj = CardFront(text=front, author=request.user)
                    card_front_obj.save()
                card_obj.front = card_front_obj
            card_obj.back = back
            card_obj.example = example
            card_obj.save()
            return render_to_response('cards/card.html', {'card': card_obj, }, context_instance=RequestContext(request))
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def update_card_level_view(request):
    if request.is_ajax() and request.method == 'POST':
        form = UpdateCardLevelForm(request.POST)
        if form.is_valid():
            pk = form.cleaned_data.get('pk')
            level_change = form.cleaned_data.get('level')
            try:
                card_obj = Card.objects.get(pk=pk, learner=request.user)
                if level_change == UpdateCardLevelForm.UP:
                    card_obj.level_up()
                elif level_change == UpdateCardLevelForm.DOWN:
                    card_obj.level_down()
                card_obj.save()
                return render_to_response('cards/card.html', {'card': card_obj, },
                                          context_instance=RequestContext(request))
            except Card.DoesNotExist:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404


@login_required
def delete_card_view(request):
    if request.is_ajax() and request.method == 'POST':
        form = DeleteCardForm(request.POST)
        if form.is_valid():
            card_id = form.cleaned_data.get('id')
            card = Card.objects.get(pk=card_id, learner=request.user)
            if card.is_public:
                card.learner = None
                card.save()
            else:
                # card_front = card.front
                # if not card_front.is_public:
                #     card_front.delete()
                card.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404
