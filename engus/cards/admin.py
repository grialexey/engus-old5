# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import CardFront, Card, Deck


class CardFrontAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_public', 'pronunciation', 'audio', 'author', 'created', )
    list_filter = ('is_public', )
    search_fields = ('text', )
    raw_id_fields = ('author', )
    exclude = ('author', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.save()


class CardAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'level', )
    raw_id_fields = ('front', 'learner', 'parent', )


class CardInline(admin.StackedInline):
    model = Card
    raw_id_fields = ('front', 'learner', 'parent', )
    extra = 1
    fields = ('front', 'back', 'example', 'image', )


class DeckAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 120, }), label=u'Заголовок')
    subtitle = forms.CharField(widget=forms.TextInput(attrs={'size': 120, }), label=u'Подзаголовок', required=False)
    description = forms.CharField(widget=CKEditorWidget(), label=u'Статья')

    class Meta:
        exclude = ('author', 'slug', )
        model = Deck


class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'subtitle', 'author', )
    form = DeckAdminForm
    inlines = [
        CardInline,
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.save()


admin.site.register(CardFront, CardFrontAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)
