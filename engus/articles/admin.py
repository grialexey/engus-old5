# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from engus.cards.models import Card
from .models import Article


class ArticleAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label=u'Статья')

    class Meta:
        fields = '__all__'
        model = Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'subtitle', 'author', )
    form = ArticleAdminForm
    raw_id_fields = ('author', )


admin.site.register(Article, ArticleAdmin)
