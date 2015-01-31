# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20150131_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='subtitle',
            field=models.CharField(max_length=255, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='back',
            field=models.CharField(max_length=255, verbose_name='\u041f\u0435\u0440\u0435\u0432\u043e\u0434', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='example',
            field=models.TextField(verbose_name='\u041f\u0440\u0438\u043c\u0435\u0440 \u0443\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='front',
            field=models.ForeignKey(verbose_name='\u0412\u0435\u0440\u0445', to='cards.CardFront'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='icon',
            field=models.ImageField(upload_to=b'card_icon/%Y_%m_%d', verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to=b'card_image/%Y_%m_%d', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='author',
            field=models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(to='cards.Card', verbose_name='\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='description',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='image',
            field=models.ImageField(upload_to=b'card_deck/%Y_%m_%d', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='\u041c\u043e\u0434\u0438\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='similar_decks',
            field=models.ManyToManyField(related_name='similar_decks_rel_+', verbose_name='\u041f\u043e\u0445\u043e\u0436\u0438\u0435 \u043d\u0430\u0431\u043e\u0440\u044b', to='cards.Deck', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deck',
            name='weight',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0412\u0435\u0441'),
            preserve_default=True,
        ),
    ]
