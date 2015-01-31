# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0005_auto_20150131_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='author',
        ),
        migrations.RemoveField(
            model_name='card',
            name='learner',
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
