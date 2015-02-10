# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import engus.utils.autoslug_field


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150210_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', engus.utils.autoslug_field.AutoSlugField(editable=False, populate_from=b'name', max_length=100, blank=True, unique=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='articletag',
            options={'verbose_name': '\u0422\u0435\u0433', 'verbose_name_plural': '\u0422\u0435\u0433\u0438'},
        ),
    ]
