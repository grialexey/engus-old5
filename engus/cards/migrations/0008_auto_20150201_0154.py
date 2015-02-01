# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20150131_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardfront',
            name='author',
        ),
        migrations.RemoveField(
            model_name='cardfront',
            name='created',
        ),
        migrations.RemoveField(
            model_name='cardfront',
            name='is_public',
        ),
    ]
