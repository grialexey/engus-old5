# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import engus.utils.autoslug_field


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-created'], 'verbose_name': '\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430', 'verbose_name_plural': '\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='deck',
            name='slug',
            field=engus.utils.autoslug_field.AutoSlugField(editable=False, populate_from=b'name', max_length=255, blank=True, unique=True),
            preserve_default=True,
        ),
    ]
