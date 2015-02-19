# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20150210_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432')),
                ('initial_number', models.PositiveIntegerField(verbose_name='\u0418\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u0440\u0442\u043e\u0447\u0435\u043a')),
                ('from_date', models.DateTimeField(verbose_name='\u0421 \u0447\u0438\u0441\u043b\u0430')),
                ('till_date', models.DateTimeField(verbose_name='\u041f\u043e \u0447\u0438\u0441\u043b\u043e')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0426\u0435\u043b\u044c',
                'verbose_name_plural': '\u0426\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
    ]
