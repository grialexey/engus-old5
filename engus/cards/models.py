# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone


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


class CardQuerySet(models.QuerySet):

    def public(self):
        return self.filter(learner=None)

    def all_for_user(self, user):
        return self.filter(learner=user)

    def new_for_user(self, user):
        return self.filter(learner=user, level=0)

    def in_learning_for_user(self, user):
        return self.filter(learner=user, level__gt=0, level__lt=5)

    def to_repeat_for_user(self, user):
        now = timezone.now()
        return self.filter(learner=user, last_repeat__isnull=False, level__lt=5).filter(Q(level=1) |
                                                                                        ~Q(last_repeat__day=now.day,
                                                                                           last_repeat__month=now.month,
                                                                                           last_repeat__year=now.year))

    def learned_for_user(self, user):
        return self.filter(learner=user, level=5)


class CardManager(models.Manager):

    def get_queryset(self):
        return super(CardManager, self).get_queryset().select_related('front')


class Card(models.Model):
    front = models.ForeignKey(CardFront, verbose_name=u'Верх')
    back = models.CharField(blank=True, max_length=255, verbose_name=u'Перевод')
    image = models.ImageField(upload_to='card_image/%Y_%m_%d', blank=True, verbose_name=u'Изображение')
    example = models.TextField(blank=True, verbose_name=u'Пример употребления')

    learner = models.ForeignKey(User, null=True, blank=True)
    level = models.IntegerField(default=0)
    last_repeat = models.DateTimeField(null=True, blank=True)
    repeat_count = models.PositiveIntegerField(default=0)

    popularity = models.IntegerField(default=0)
    learned = models.DateTimeField(null=True, blank=True, verbose_name=u'Запомнена')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')

    objects = CardManager().from_queryset(CardQuerySet)()

    # def is_public(self):
    #     return self.deck is None

    def is_repeated_today(self):
        return self.last_repeat is not None and (self.last_repeat.date() == timezone.now().date()) and self.level > 1

    def level_up(self):
        if not self.is_repeated_today():
            if self.level == 0:
                self.level = 2
            elif self.level < 5:
                self.level += 1
            elif self.level == 5 and self.learned is None:
                self.learned = timezone.now()
            self.last_repeat = timezone.now()
            self.repeat_count += 1

    def level_down(self):
        if not self.level == 1:
            self.level = 1
            self.learned = None
            self.last_repeat = timezone.now()
            self.repeat_count += 1

    def add_card_front(self, text, user):
        try:
            card_front_obj = CardFront.objects.filter(text__iexact=text, is_public=True)[0]
        except IndexError:
            card_front_obj = CardFront.objects.create(text=text, author=user)
        self.front = card_front_obj

    class Meta:
        verbose_name = u'Карточка'
        verbose_name_plural = u'Карточки'
        ordering = ['-created', ]

    def __unicode__(self):
        return u'#%d. %s – %s' % (self.pk, self.front.text, self.back)

