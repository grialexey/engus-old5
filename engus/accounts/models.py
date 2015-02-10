# -*- coding: utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User


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
