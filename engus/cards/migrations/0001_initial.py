# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import engus.utils.autoslug_field
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('back', models.CharField(max_length=255, blank=True)),
                ('image', models.ImageField(upload_to=b'card_image/%Y_%m_%d', blank=True)),
                ('icon', models.ImageField(upload_to=b'card_icon/%Y_%m_%d', blank=True)),
                ('example', models.TextField(blank=True)),
                ('level', models.IntegerField(default=0, choices=[(-2, '\u041e\u0447\u0435\u043d\u044c \u043f\u043b\u043e\u0445\u043e'), (-1, '\u041f\u043b\u043e\u0445\u043e'), (0, '\u041d\u043e\u0432\u0430\u044f'), (1, '\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u043b'), (2, '\u0425\u043e\u0440\u043e\u0448\u043e \u0437\u0430\u043f\u043e\u043c\u043d\u0438\u043b')])),
                ('popularity', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': '\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardFront',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('pronunciation', models.CharField(max_length=255, blank=True)),
                ('audio', models.FileField(upload_to=b'cards_audio/%Y_%m_%d', blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430')),
            ],
            options={
                'verbose_name': '\u0412\u0435\u0440\u0445 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438',
                'verbose_name_plural': '\u0412\u0435\u0440\u0445 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435\u043a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', engus.utils.autoslug_field.AutoSlugField(populate_from=(b'name',), max_length=255, editable=False, blank=True)),
                ('image', models.ImageField(upload_to=b'card_deck/%Y_%m_%d', blank=True)),
                ('description', models.TextField(blank=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cards', models.ManyToManyField(to='cards.Card', blank=True)),
                ('similar_decks', models.ManyToManyField(related_name='similar_decks_rel_+', to='cards.Deck', blank=True)),
            ],
            options={
                'ordering': ['-weight', 'name'],
                'verbose_name': '\u041d\u0430\u0431\u043e\u0440',
                'verbose_name_plural': '\u041d\u0430\u0431\u043e\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='front',
            field=models.ForeignKey(to='cards.CardFront'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='parent',
            field=models.ForeignKey(blank=True, to='cards.Card', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
