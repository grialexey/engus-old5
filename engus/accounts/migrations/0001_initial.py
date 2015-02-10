# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d')),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('registered_user', models.OneToOneField(related_name='registration_invite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': '\u0418\u043d\u0432\u0430\u0439\u0442',
                'verbose_name_plural': '\u0418\u043d\u0432\u0430\u0439\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
