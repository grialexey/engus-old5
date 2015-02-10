# -*- coding: utf-8 -*-
from django import forms
from ckeditor.widgets import CKEditorWidget
from django_select2.fields import AutoModelSelect2TagField
from .models import Article, ArticleTag


class TagField(AutoModelSelect2TagField):
    queryset = ArticleTag.objects.all()
    search_fields = ['name__icontains', ]

    def get_model_field_values(self, value):
        return {'name': value, }