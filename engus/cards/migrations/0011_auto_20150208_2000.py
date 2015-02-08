# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20150202_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='cards',
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u0431\u043e\u0440', blank=True, to='cards.Deck', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
