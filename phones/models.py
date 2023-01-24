from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=200, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.URLField(verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(default=True, verbose_name='В наличии')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'