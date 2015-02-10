# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20150210_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-rating', '-published'], 'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
    ]
