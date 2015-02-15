# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0018_auto_20150212_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='copy_from',
            field=models.ForeignKey(related_name='copy_set', verbose_name='\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0430 \u0441', blank=True, to='cards.Card', null=True),
            preserve_default=True,
        ),
    ]
