# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0019_card_copy_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardfront',
            name='audio',
            field=models.FileField(upload_to=b'word/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
    ]
