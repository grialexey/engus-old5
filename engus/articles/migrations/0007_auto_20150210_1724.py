# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published'], 'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='articlerating',
            unique_together=set([('article', 'user')]),
        ),
    ]
