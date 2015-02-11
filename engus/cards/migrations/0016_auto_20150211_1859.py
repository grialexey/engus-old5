# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_card_learned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='last_repeat',
        ),
        migrations.RemoveField(
            model_name='card',
            name='learned',
        ),
        migrations.RemoveField(
            model_name='card',
            name='popularity',
        ),
        migrations.AddField(
            model_name='card',
            name='next_repeat',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='level',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
