# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from ckeditor.widgets import CKEditorWidget
from .models import Article, ArticleCategory, ArticleTag, ArticleRating


class ArticleAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label=u'Статья')

    class Meta:
        fields = '__all__'
        model = Article

    def __init__(self, *args, **kwargs):
        super(ArticleAdminForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = ArticleTag.objects.all()


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published', 'is_approved', 'author', 'created', 'modified',
                    'published', 'rating', )
    form = ArticleAdminForm
    raw_id_fields = ('author', )
    filter_horizontal = ('cards', 'tags', )
    list_filter = ('is_published', 'is_approved', )
    ordering = ('published', )


class ArticleRatingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user', 'positive', 'created', )
    raw_id_fields = ('user', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(ArticleTag)
admin.site.register(ArticleRating, ArticleRatingAdmin)
