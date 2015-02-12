# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20150211_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published'], 'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b', 'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0437\u0434\u0435\u043b', to='articles.ArticleCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='level',
            field=models.IntegerField(verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0432\u043b\u0430\u0434\u0435\u043d\u0438\u044f \u044f\u0437\u044b\u043a\u043e\u043c', choices=[(1, 'Beginner (\u0434\u043b\u044f \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0445)'), (2, 'Elementary'), (3, 'Intermediate'), (4, 'Upper-Intermediate'), (5, 'Advanced')]),
            preserve_default=True,
        ),
    ]
