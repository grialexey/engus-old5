# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20150131_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='user',
            new_name='learner',
        ),
    ]
