from django.db import models


class BrandCar(models.Model):
    brand = models.CharField(verbose_name='Марка', max_length=50)
    slug = models.SlugField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'


class ModelCar(models.Model):
    model = models.CharField(verbose_name='Модель', max_length=50)
    slug = models.SlugField(max_length=200, blank=False, null=False)
    body = models.CharField(verbose_name='Кузов', max_length=50)
    price = models.PositiveIntegerField(verbose_name='Цена')
    year_of_issue = models.PositiveIntegerField(verbose_name='Год выпуска')
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    engine_volume = models.FloatField(verbose_name='Объём двигателя')
    engine_type = models.CharField(verbose_name='Тип двигателя', max_length=20)
    engine_power = models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')
    transmission = models.CharField(verbose_name='Коробка передач', max_length=20)
    drive_unit = models.CharField(verbose_name='Привод', max_length=20)
    color = models.CharField(verbose_name='Цвет', max_length=50)
    description = models.CharField(verbose_name='Описание', max_length=150)
    equipment = models.TextField(verbose_name='Комплектация')
    brand = models.ForeignKey(to='BrandCar', on_delete=models.DO_NOTHING, db_index=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели'
