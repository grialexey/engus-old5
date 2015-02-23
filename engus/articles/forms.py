# -*- coding: utf-8 -*-
from django import forms
from django.http import HttpResponseRedirect
from ckeditor.widgets import CKEditorWidget
from django_select2.fields import AutoModelSelect2TagField
from .models import Article, ArticleTag


class ArticleTagsField(AutoModelSelect2TagField):
    queryset = ArticleTag.objects
    search_fields = ['name__icontains', ]

    def get_model_field_values(self, value):
        return {'name': value, }


class ArticleForm(forms.ModelForm):
    tags = ArticleTagsField(label=u'Теги', required=False)
    description = forms.CharField(widget=CKEditorWidget(), label=u'Статья', required=False)

    class Meta:
        model = Article
        fields = ['name', 'subtitle', 'image', 'category', 'level', 'description', 'tags', ]


class ArticleUpdateForm(ArticleForm):

    class Meta:
        model = Article
        fields = ['name', 'subtitle', 'image', 'category', 'level', 'description', 'tags', 'is_published', ]
