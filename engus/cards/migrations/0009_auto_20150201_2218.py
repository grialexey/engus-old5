# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0008_auto_20150201_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardfront',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardfront',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 18, 18, 20, 916186, tzinfo=utc), verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardfront',
            name='is_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
