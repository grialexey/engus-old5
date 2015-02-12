# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0016_auto_20150211_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='learner',
            field=models.ForeignKey(related_name='learning_card_set', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
