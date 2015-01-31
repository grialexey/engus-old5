# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from .models import Deck


class DeckDetailView(DetailView):

    context_object_name = 'deck'
    model = Deck