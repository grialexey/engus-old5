# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0010_remove_article_cards'),
        ('cards', '0017_auto_20150212_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='learner',
        ),
        migrations.AddField(
            model_name='card',
            name='article',
            field=models.ForeignKey(verbose_name='\u0421\u0442\u0430\u0442\u044c\u044f', blank=True, to='articles.Article', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(default=1, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
