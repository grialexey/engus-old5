# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150219_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='invite',
            name='registered_user',
        ),
        migrations.DeleteModel(
            name='Invite',
        ),
        migrations.AlterField(
            model_name='cardsgoal',
            name='initial_number',
            field=models.PositiveIntegerField(verbose_name='\u0418\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0443\u0447\u0435\u043d\u043d\u044b\u0445 \u0441\u043b\u043e\u0432'),
            preserve_default=True,
        ),
    ]
