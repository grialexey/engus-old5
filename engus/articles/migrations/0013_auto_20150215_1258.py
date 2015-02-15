# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20150213_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='level',
            field=models.CharField(default=b'elementary', max_length=100, verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0432\u043b\u0430\u0434\u0435\u043d\u0438\u044f \u044f\u0437\u044b\u043a\u043e\u043c', choices=[(b'elementary', 'Elementary'), (b'intermediate', 'Intermediate'), (b'advanced', 'Advanced')]),
            preserve_default=True,
        ),
    ]
