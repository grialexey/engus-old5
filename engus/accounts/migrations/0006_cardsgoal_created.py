# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150221_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardsgoal',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 22, 8, 45, 47, 285690, tzinfo=utc), verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430', auto_now_add=True),
            preserve_default=False,
        ),
    ]
