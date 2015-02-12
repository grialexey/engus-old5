# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import CardFront, Card


class CardFrontAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_public', 'pronunciation', 'audio', 'author', 'created', )
    list_filter = ('is_public', )
    search_fields = ('text', )
    raw_id_fields = ('author', )


class CardAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'level', 'next_repeat', 'user', 'created', )
    raw_id_fields = ('front', 'user', )


admin.site.register(CardFront, CardFrontAdmin)
admin.site.register(Card, CardAdmin)
