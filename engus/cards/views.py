# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from .models import Deck, Card, CardFront
from .forms import NewCardForm


class DeckDetailView(DetailView):

    context_object_name = 'deck'
    model = Deck


class MyCardListView(LoginRequiredMixin, ListView):

    template_name = 'cards/my_card_list.html'

    def get_queryset(self):
        return Card.objects.filter(learner=self.request.user)


@login_required
def create_new_card_ajax_view(request):
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