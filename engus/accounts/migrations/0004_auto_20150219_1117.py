# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cardsgoal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardsgoal',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='cardsgoal',
            name='till_date',
        ),
        migrations.AddField(
            model_name='cardsgoal',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 7, 17, 11, 16647, tzinfo=utc), verbose_name='\u0424\u0438\u043d\u0438\u0448'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardsgoal',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 7, 17, 17, 510938, tzinfo=utc), verbose_name='\u0421\u0442\u0430\u0440\u0442'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardsgoal',
            name='user',
            field=models.OneToOneField(related_name='goal', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
