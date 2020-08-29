from datetime import datetime
from os.path import splitext

from django.db import models


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(),
                     splitext(filename)[1])


class Img(models.Model):
    img = models.ImageField(verbose_name='Изображение',
                            upload_to=get_timestamp_path)
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'
        ordering = ['desc']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    image = models.ImageField(null=True, verbose_name='Изображение')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-published']
