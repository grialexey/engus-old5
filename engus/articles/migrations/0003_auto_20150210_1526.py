# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import engus.utils.autoslug_field


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_similar_decks'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletag',
            name='slug',
            field=engus.utils.autoslug_field.AutoSlugField(editable=False, populate_from=b'name', max_length=100, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='level',
            field=models.IntegerField(verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c', choices=[(1, 'Beginner'), (2, 'Elementary'), (3, 'Intermediate'), (4, 'Upper-Intermediate'), (5, 'Advanced')]),
            preserve_default=True,
        ),
    ]
