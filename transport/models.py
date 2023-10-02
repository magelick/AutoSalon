from django.db import models


class BrandCar(models.Model):
    # Бренд (марка): Volkswagen
    brand = models.CharField(verbose_name='Марка', max_length=50)
    slug = models.SlugField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'


class ModelCar(models.Model):
    # Модель марки: Passat
    model = models.CharField(verbose_name='Модель', max_length=50)
    slug = models.SlugField(max_length=200, blank=False, null=False)
    brand = models.ForeignKey(
        to="BrandCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="models"
    )

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели'


class BodyCar(models.Model):
    # Кузов модели: B3 и B8
    body = models.CharField(verbose_name='Кузов', max_length=50)
    slug = models.SlugField(max_length=200, blank=False, null=False)
    model = models.ForeignKey(
        to='ModelCar',
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name='bodies'
    )

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'кузов'
        verbose_name_plural = 'кузова'


class EngineType(models.Model):
    # Тип двигателя: бензин, дизель, электро
    engine_type = models.CharField(
        verbose_name='Тип двигателя',
        max_length=20)

    def __str__(self):
        return self.engine_type

    class Meta:
        verbose_name = 'тип двигателя'
        verbose_name_plural = 'типы двигателей'


class TransmissionType(models.Model):
    # Коробка передач: автомат, механика
    transmission = models.CharField(
        verbose_name='Коробка передач',
        max_length=20)

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = 'коробка передач'
        verbose_name_plural = 'коробки передач'


class DriveUnitType(models.Model):
    # Тип привод: полный, передний, задний
    drive_unit = models.CharField(
        verbose_name='Привод',
        max_length=20)

    def __str__(self):
        return self.drive_unit

    class Meta:
        verbose_name = 'тип привода'
        verbose_name_plural = 'типы приводов'


class BodyTypeCar(models.Model):
    # Тип кузова: внедорожник, кабриолет, седан, купе и т.д.
    type_body = models.CharField(
        verbose_name='Тип кузова',
        max_length=50)

    def __str__(self):
        return self.type_body

    class Meta:
        verbose_name = 'тип кузова'
        verbose_name_plural = 'типы кузова'


class ColorType(models.Model):
    # Цвет кузова
    color = models.CharField(
        verbose_name='Цвет',
        max_length=50
    )

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'


class AnnouncementCar(models.Model):
    # Конкретное объявление
    car_brand = models.ForeignKey(
        to="BrandCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='бренд'
    )
    car_model = models.ForeignKey(
        to="ModelCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='модель'
    )
    car_body = models.ForeignKey(
        to="BodyCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='кузов'
    )
    car_engine_type = models.ForeignKey(
        to="EngineType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип двигателя'
    )
    car_transmission_type = models.ForeignKey(
        to="TransmissionType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип коробки передач'
    )
    car_drive_unit_type = models.ForeignKey(
        to="DriveUnitType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип привода'
    )
    car_body_type = models.ForeignKey(
        to="BodyTypeCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип кузова'
    )
    car_color_type = models.ForeignKey(
        to="ColorType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='цвет'
    )
    price = models.PositiveIntegerField(verbose_name='Цена')
    year_of_issue = models.PositiveIntegerField(verbose_name='Год выпуска')
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    engine_volume = models.FloatField(verbose_name='Объём двигателя')
    engine_power = models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')
    description = models.TextField(verbose_name='Описание')
    equipment = models.TextField(verbose_name='Комплектация')
    announcement_car_slug = models.SlugField(
        max_length=200,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
