# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20150212_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='level',
            field=models.IntegerField(verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0432\u043b\u0430\u0434\u0435\u043d\u0438\u044f \u044f\u0437\u044b\u043a\u043e\u043c', choices=[(1, 'Beginner'), (2, 'Elementary'), (3, 'Intermediate'), (4, 'Upper-Intermediate'), (5, 'Advanced')]),
            preserve_default=True,
        ),
    ]
