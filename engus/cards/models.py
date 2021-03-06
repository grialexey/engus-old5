# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone


class CardFront(models.Model):
    text = models.CharField(max_length=255)
    pronunciation = models.CharField(blank=True, max_length=255)
    audio = models.FileField(blank=True, upload_to='word/%Y_%m_%d')
    is_public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = u'Верх карточки'
        verbose_name_plural = u'Верх карточкек'

    def __unicode__(self):
        return self.text


class CardQuerySet(models.QuerySet):

    def public(self):
        return self.filter(article__isnull=False).order_by('created')

    def learning(self):
        return self.filter(article__isnull=True)

    def to_repeat(self):
        return self.learning().filter(next_repeat__lt=timezone.now())

    def learned(self):
        return self.learning().filter(next_repeat__gt=timezone.now())


class CardManager(models.Manager):

    def get_queryset(self):
        return super(CardManager, self).get_queryset().select_related('front')


class Card(models.Model):
    front = models.ForeignKey(CardFront, verbose_name=u'Верх')
    back = models.CharField(blank=True, max_length=255, verbose_name=u'Перевод')
    image = models.ImageField(upload_to='card_image/%Y_%m_%d', blank=True, verbose_name=u'Изображение')
    example = models.TextField(blank=True, verbose_name=u'Пример употребления')
    user = models.ForeignKey(User, verbose_name=u'Создатель')
    level = models.PositiveIntegerField(default=0)
    next_repeat = models.DateTimeField(default=timezone.now)
    repeat_count = models.PositiveIntegerField(default=0)
    article = models.ForeignKey('articles.Article', null=True, blank=True, verbose_name=u'Статья')
    copy_from = models.ForeignKey('self', null=True, blank=True, related_name='copy_set', verbose_name=u'Скопирована с')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')

    objects = CardManager().from_queryset(CardQuerySet)()

    def is_to_repeat(self):
        return self.article is not None or self.next_repeat < timezone.now()

    def set_next_repeat(self):
        now = timezone.now()
        if self.level == 0 and self.next_repeat > now:
            self.next_repeat = now
        elif self.level == 1:
            self.next_repeat = now + datetime.timedelta(minutes=20)
        elif self.level == 2:
            self.next_repeat = now + datetime.timedelta(hours=2)
        elif self.level == 3:
            self.next_repeat = now + datetime.timedelta(hours=8)
        elif self.level == 4:
            self.next_repeat = now + datetime.timedelta(hours=24)
        elif self.level == 5:
            self.next_repeat = now + datetime.timedelta(hours=72)
        elif self.level == 6:
            self.next_repeat = now + datetime.timedelta(weeks=2)
        elif self.level == 7:
            self.next_repeat = now + datetime.timedelta(weeks=6)
        elif self.level > 7:
            self.next_repeat = now + datetime.timedelta(weeks=52)

    def good(self):
        if self.is_to_repeat():
            self.level += 1
            self.repeat_count += 1
            self.set_next_repeat()

    def bad(self):
        self.level = 0
        self.repeat_count += 1
        self.set_next_repeat()

    def add_card_front(self, text, user):
        try:
            card_front_obj = CardFront.objects.filter(text__iexact=text, is_public=True)[0]
        except IndexError:
            card_front_obj = CardFront.objects.create(text=text, author=user)
        self.front = card_front_obj

    def make_copy(self, user):
        new_card = Card()
        new_card.copy_from = self
        new_card.front = self.front
        new_card.image = self.image
        new_card.back = self.back
        new_card.example = self.example
        new_card.user = user
        return new_card

    class Meta:
        verbose_name = u'Карточка'
        verbose_name_plural = u'Карточки'
        ordering = ['-created', ]

    def __unicode__(self):
        return u'#%d. %s – %s' % (self.pk, self.front.text, self.back)

