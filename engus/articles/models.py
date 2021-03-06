# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from engus.utils.autoslug_field import AutoSlugField, ru_slugify_fn


class ArticleQuerySet(models.QuerySet):

    def published(self):
        return self.filter(is_published=True, is_approved=True, published__lt=timezone.now)


class ArticleManager(models.Manager):

    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().select_related('category')


class Article(models.Model):
    BEGINNER = 'beginner'
    ELEMENTARY = 'elementary'
    PRE_INTERMEDIATE = 'pre-intermediate'
    INTERMEDIATE = 'intermediate'
    UPPER_INTERMEDIATE = 'upper-intermediate'
    ADVANCED = 'advanced'
    PROFICIENCY = 'proficiency'

    LEVEL_CHOICES = (
        (ELEMENTARY, u'Elementary'),
        (INTERMEDIATE, u'Intermediate'),
        (ADVANCED, u'Advanced'),
    )

    name = models.CharField(max_length=255, verbose_name=u'Заголовок')
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True, editable=True,
                         slugify_function=ru_slugify_fn)
    subtitle = models.CharField(max_length=255, blank=True, verbose_name=u'Подзаголовок')
    category = models.ForeignKey('ArticleCategory', verbose_name=u'Раздел')
    image = models.ImageField(upload_to="article/%Y_%m_%d", blank=True, verbose_name=u'Изображение')
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default=ELEMENTARY,
                             verbose_name=u'Уровень владения языком')
    tags = models.ManyToManyField('ArticleTag', blank=True, null=True, verbose_name=u'Теги')
    description = models.TextField(blank=True, verbose_name=u'Текст')
    rating = models.IntegerField(default=0, verbose_name=u'Рейтинг')
    is_published = models.BooleanField(default=False, verbose_name=u'Опубликовано')
    is_approved = models.BooleanField(default=True, verbose_name=u'Одобрена')
    author = models.ForeignKey(User, verbose_name=u'Автор')
    published = models.DateTimeField(null=True, blank=True, verbose_name=u'Опубликована')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'Редактирована')

    objects = ArticleManager().from_queryset(ArticleQuerySet)()

    class Meta:
        ordering = ['-published', ]
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.published is None and self.is_published and self.is_approved:
            self.published = timezone.now()
        super(Article, self).save(*args, **kwargs)

    def calculate_rating(self):
        self.rating = 0
        for rating in self.articlerating_set.all():
            if rating.positive:
                self.rating += 1
            else:
                self.rating -= 1

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'category': self.category.slug, 'slug': self.slug, })


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', max_length=100, unique=True, editable=True,
                         slugify_function=ru_slugify_fn)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Раздел'
        verbose_name_plural = u'Разделы'

    def get_absolute_url(self):
        return reverse('articles:article-list', kwargs={'category': self.slug, })


class ArticleRating(models.Model):
    article = models.ForeignKey(Article, verbose_name=u'Статья')
    positive = models.BooleanField(default=True, verbose_name=u'Положительная')
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создана')

    class Meta:
        ordering = ['-created', ]
        verbose_name = u'Оценка для статьи'
        verbose_name_plural = u'Оценки для статьи'
        unique_together = ('article', 'user', )

    def __unicode__(self):
        return self.article.name

    def save(self, *args, **kwargs):
        super(ArticleRating, self).save(*args, **kwargs)
        self.article.calculate_rating()
        self.article.save()


class ArticleTag(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', max_length=100, unique=True, editable=True,
                         slugify_function=ru_slugify_fn)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'