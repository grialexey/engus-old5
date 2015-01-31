# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CardFront, Card, Deck


admin.site.register(CardFront)
admin.site.register(Card)
admin.site.register(Deck)
