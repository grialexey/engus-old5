# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_auto_20150201_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='last_repeat',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='repeat_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='level',
            field=models.IntegerField(default=0, choices=[(-2, '\u0417\u0430\u0431\u044b\u043b'), (-1, '\u041a \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044e'), (0, '\u041d\u043e\u0432\u0430\u044f'), (1, '\u0425\u043e\u0440\u043e\u0448\u043e'), (2, '\u041e\u0442\u043b\u0438\u0447\u043d\u043e'), (3, '\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u043b')]),
            preserve_default=True,
        ),
    ]
