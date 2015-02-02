# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from .models import Deck, Card, CardFront
from .forms import NewCardForm, DeleteCardForm


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
        form = NewCardForm(request.POST)
        if form.is_valid():
            card_front = form.cleaned_data.get('front').strip()
            card_back = form.cleaned_data.get('back', '').strip()
            try:
                card_front_obj = CardFront.objects.get(text__iexact=card_front, is_public=True)
            except CardFront.DoesNotExist:
                card_front_obj = CardFront(text=card_front, author=request.user)
                card_front_obj.save()
            Card.objects.create(front=card_front_obj, back=card_back, learner=request.user)
            return HttpResponse(status=201)
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
                card_front = card.front
                if not card_front.is_public:
                    card_front.delete()
                card.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()
    else:
        raise Http404
