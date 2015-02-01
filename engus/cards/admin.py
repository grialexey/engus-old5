# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CardFront, Card, Deck


class CardFrontAdmin(admin.ModelAdmin):
    list_display = ('text', 'pronunciation', 'audio', )


class CardAdmin(admin.ModelAdmin):
    raw_id_fields = ['front', ]


admin.site.register(CardFront, CardFrontAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Deck)
