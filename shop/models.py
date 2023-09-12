from django.db import models


class Shop(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    descr = models.TextField(verbose_name='Описание')
    phone = models.CharField(verbose_name='Контактный номер', max_length=100)
    about_us = models.TextField(verbose_name='О нас')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'

