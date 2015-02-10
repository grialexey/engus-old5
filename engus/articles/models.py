# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from engus.utils.autoslug_field import AutoSlugField, ru_slugify_fn


class Article(models.Model):
    BEGINNER = 1
    ELEMENTARY = 2
    INTERMEDIATE = 3
    UPPER_INTERMEDIATE = 4
    ADVANCED = 5

    LEVEL_CHOICES = (
        (BEGINNER, u'Beginner'),
        (ELEMENTARY, u'Elementary'),
        (INTERMEDIATE, u'Intermediate'),
        (UPPER_INTERMEDIATE, u'Upper-Intermediate'),
        (ADVANCED, u'Advanced'),
    )

    name = models.CharField(max_length=255, verbose_name=u'Заголовок')
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True, editable=True,
                         slugify_function=ru_slugify_fn)
    subtitle = models.CharField(max_length=255, blank=True, verbose_name=u'Подзаголовок')
    image = models.ImageField(upload_to="card_deck/%Y_%m_%d", blank=True, verbose_name=u'Изображение')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name=u'Уровень')
    tags = models.ManyToManyField('ArticleTag', blank=True, null=True, verbose_name=u'Теги')
    description = models.TextField(blank=True, verbose_name=u'Текст')
    cards = models.ManyToManyField('cards.Card', blank=True, null=True, verbose_name=u'Карточки')

    is_published = models.BooleanField(default=False, verbose_name=u'Опубликовано')
    is_approved = models.BooleanField(default=True, verbose_name=u'Одобрена')
    author = models.ForeignKey(User, verbose_name=u'Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'Редактирована')

    class Meta:
        ordering = ['-created', ]
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'slug': self.slug, })


class ArticleRating(models.Model):
    article = models.ForeignKey(Article, verbose_name=u'Статья')
    positive = models.BooleanField(default=True, verbose_name=u'Положительная')
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')

    class Meta:
        ordering = ['-created', ]
        verbose_name = u'Оценка для статьи'
        verbose_name_plural = u'Оценки для статьи'

    def __unicode__(self):
        return self.article


class ArticleTag(models.Model):
    name = models.CharField(max_length=100)