# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_remove_card_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='learned',
            field=models.DateTimeField(null=True, verbose_name='\u0417\u0430\u043f\u043e\u043c\u043d\u0435\u043d\u0430', blank=True),
            preserve_default=True,
        ),
    ]
