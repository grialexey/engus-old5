# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0012_remove_card_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='author',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='similar_decks',
        ),
        migrations.RemoveField(
            model_name='card',
            name='deck',
        ),
        migrations.DeleteModel(
            name='Deck',
        ),
    ]
