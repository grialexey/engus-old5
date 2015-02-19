# -*- coding: utf-8 -*-
import os
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from engus.cards.models import Card


class Invite(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True)
    registered_user = models.OneToOneField(User, null=True, blank=True, related_name='registration_invite')
    code = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создан')

    class Meta:
        verbose_name = u'Инвайт'
        verbose_name_plural = u'Инвайты'
        ordering = ('-created', )

    def generate_unique_code(self):
        while 1:
            random_code = os.urandom(7).encode('hex')
            try:
                Invite.objects.get(code=random_code)
            except Invite.DoesNotExist:
                self.code = random_code
                break

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate_unique_code()
        super(Invite, self).save(*args, **kwargs)


class CardsGoal(models.Model):
    user = models.OneToOneField(User, related_name='goal')
    number = models.PositiveIntegerField(verbose_name=u'Количество слов')
    initial_number = models.PositiveIntegerField(verbose_name=u'Изначальное количество выученных слов')
    start = models.DateTimeField(verbose_name=u'Старт')
    finish = models.DateTimeField(verbose_name=u'Финиш')

    class Meta:
        verbose_name = u'Цель'
        verbose_name_plural = u'Цели'

    def is_active(self):
        return self.start < timezone.now() < self.finish

    def is_completed(self):
        return Card.objects.filter(user=self.user).learned().count() > self.number

    def cards_to_learn(self):
        return self.number - self.initial_number

    def progress_in_cards(self):
        progress_in_cards = Card.objects.filter(user=self.user).learned().count() - self.initial_number
        if progress_in_cards < 0:
            progress_in_cards = 0
        return progress_in_cards

    def progress_in_percent(self):
        return float(self.progress_in_cards()) / float(self.cards_to_learn()) * 100

    def scheduled(self, date_time):
        cards_to_learn = self.number - self.initial_number
        total_time_in_seconds = (self.finish - self.start).total_seconds()
        time_to_date_in_seconds = (date_time - self.start).total_seconds()
        scheduled = (cards_to_learn / (total_time_in_seconds / time_to_date_in_seconds)) + self.initial_number
        return int(scheduled)

    def cards_a_day(self):
        cards_to_learn = self.number - self.initial_number
        total_time_in_seconds = (self.finish - self.start).total_seconds()
        one_day_in_seconds = datetime.timedelta(days=1).total_seconds()
        cards_a_day = cards_to_learn / (total_time_in_seconds / one_day_in_seconds)
        return int(cards_a_day)

    def behind_the_schedule(self, date_time):
        return Card.objects.filter(user=self.user).learned().count() - self.scheduled(date_time)

    def behind_the_schedule_for_now(self):
        return self.behind_the_schedule(timezone.now())
