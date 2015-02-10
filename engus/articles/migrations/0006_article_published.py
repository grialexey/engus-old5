# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateTimeField(null=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u0430', blank=True),
            preserve_default=True,
        ),
    ]
