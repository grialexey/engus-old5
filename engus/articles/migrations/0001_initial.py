# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import engus.utils.autoslug_field
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_remove_card_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', engus.utils.autoslug_field.AutoSlugField(editable=False, populate_from=b'name', max_length=255, blank=True, unique=True)),
                ('subtitle', models.CharField(max_length=255, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('image', models.ImageField(upload_to=b'card_deck/%Y_%m_%d', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                ('level', models.IntegerField(choices=[(1, '\u0414\u043b\u044f \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0445'), (2, 'Elementary'), (3, 'Intermediate'), (4, 'Upper-Intermediate'), (5, 'Advanced')])),
                ('description', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('is_approved', models.BooleanField(default=True, verbose_name='\u041e\u0434\u043e\u0431\u0440\u0435\u043d\u0430')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0430')),
                ('author', models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
                ('cards', models.ManyToManyField(to='cards.Card', null=True, verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0438', blank=True)),
                ('similar_decks', models.ManyToManyField(related_name='similar_decks_rel_+', verbose_name='\u041f\u043e\u0445\u043e\u0436\u0438\u0435 \u043d\u0430\u0431\u043e\u0440\u044b', to='articles.Article', blank=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive', models.BooleanField(default=True, verbose_name='\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430')),
                ('article', models.ForeignKey(verbose_name='\u0421\u0442\u0430\u0442\u044c\u044f', to='articles.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u041e\u0446\u0435\u043d\u043a\u0430 \u0434\u043b\u044f \u0441\u0442\u0430\u0442\u044c\u0438',
                'verbose_name_plural': '\u041e\u0446\u0435\u043d\u043a\u0438 \u0434\u043b\u044f \u0441\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='articles.ArticleTag', null=True, verbose_name='\u0422\u0435\u0433\u0438', blank=True),
            preserve_default=True,
        ),
    ]
