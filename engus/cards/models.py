# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from engus.utils.autoslug_field import AutoSlugField, ru_slugify_fn


class CardFront(models.Model):
    text = models.CharField(max_length=255)
    pronunciation = models.CharField(blank=True, max_length=255)
    audio = models.FileField(blank=True, upload_to='cards_audio/%Y_%m_%d')
    is_public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = u'Верх карточки'
        verbose_name_plural = u'Верх карточкек'

    def __unicode__(self):
        return self.text


class CardManager(models.Manager):

    def get_queryset(self):
        return super(CardManager, self).get_queryset().select_related('front')


class Card(models.Model):
    front = models.ForeignKey(CardFront, verbose_name=u'Верх')
    back = models.CharField(blank=True, max_length=255, verbose_name=u'Перевод')
    image = models.ImageField(upload_to='card_image/%Y_%m_%d', blank=True, verbose_name=u'Изображение')
    icon = models.ImageField(upload_to='card_icon/%Y_%m_%d', blank=True, verbose_name=u'Иконка')
    example = models.TextField(blank=True, verbose_name=u'Пример употребления')

    learner = models.ForeignKey(User, null=True, blank=True)
    level = models.IntegerField(default=0)
    last_repeat = models.DateTimeField(null=True, blank=True)
    repeat_count = models.PositiveIntegerField(default=0)

    is_public = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True)
    popularity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')

    objects = CardManager()

    def level_up(self):
        if self.level < 5:
            self.last_repeat = timezone.now()
            self.level += 1
            self.repeat_count += 1

    def level_down(self):
        self.level = 1
        self.last_repeat = timezone.now()
        self.repeat_count += 1

    class Meta:
        verbose_name = u'Карточка'
        verbose_name_plural = u'Карточки'
        ordering = ['-created', ]

    def __unicode__(self):
        return u'#%d. %s – %s' % (self.pk, self.front.text, self.back)


class Deck(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Заголовок')
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True, editable=True,
                         slugify_function=ru_slugify_fn)
    subtitle = models.CharField(max_length=255, blank=True, verbose_name=u'Подзаголовок')
    cards = models.ManyToManyField(Card, blank=True, verbose_name=u'Карточки')
    image = models.ImageField(upload_to="card_deck/%Y_%m_%d", blank=True, verbose_name=u'Изображение')
    description = models.TextField(blank=True, verbose_name=u'Текст')
    similar_decks = models.ManyToManyField('self', blank=True, verbose_name=u'Похожие наборы')
    weight = models.PositiveIntegerField(default=0, verbose_name=u'Вес')
    author = models.ForeignKey(User, verbose_name=u'Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'Модифицирована')

    class Meta:
        ordering = ['-weight', 'name', ]
        verbose_name = u'Набор'
        verbose_name_plural = u'Наборы'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cards:deck-detail', kwargs={'slug': self.slug, })

