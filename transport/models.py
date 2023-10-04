from datetime import datetime
from django.db.models.functions import Length
from django.db import models
from django.db.models import Q

models.CharField.register_class_lookup(Length)


class BrandCar(models.Model):
    # Бренд (марка): Volkswagen
    brand_name = models.CharField(
        verbose_name='марка',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'
        constraints = (
            models.CheckConstraint(check=Q(brand_name__lenght__lte=50), name="brand_name__lenght__lte"),
            models.CheckConstraint(check=Q(brand_name__lengt__gte=0), name="brand_name__lenght__gte")
        )


class ModelCar(models.Model):
    # Модель марки: Passat
    model_name = models.CharField(
        verbose_name='модель',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    brand = models.ForeignKey(
        to="BrandCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="models"
    )

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели'
        constraints = (
            models.CheckConstraint(check=Q(model_name__lenght__lte=50), name="model_name__length__lte"),
            models.CheckConstraint(check=Q(model_name__lenght__gte=0), name="model_name__lenght__gte")
        )


class BodyCar(models.Model):
    # Кузов модели: B3 и B8
    body_name = models.CharField(
        verbose_name='кузов',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    model = models.ForeignKey(
        to='ModelCar',
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name='bodies'
    )

    def __str__(self):
        return self.body_name

    class Meta:
        verbose_name = 'кузов'
        verbose_name_plural = 'кузова'
        constraints = (
            models.CheckConstraint(check=Q(body_name__lenght__lte=50), name="body_name__lenght__lte"),
            models.CheckConstraint(check=Q(body_name__lenght__gte=0), name="body_name__lenght__gte")
        )


class EngineTypeCar(models.Model):
    # Тип двигателя: бензин, дизель, электро
    engine = models.CharField(
        verbose_name='тип двигателя',
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.engine

    class Meta:
        verbose_name = 'тип двигателя'
        verbose_name_plural = 'типы двигателей'
        constraints = (
            models.CheckConstraint(check=Q(engine__lenght__lte=20), name="engine__lenght__lte"),
            models.CheckConstraint(check=Q(engine__lenght__gte=0), name="engine__lenght__gte")
        )


class TransmissionType(models.Model):
    # Коробка передач: автомат, механика
    transmission = models.CharField(
        verbose_name='коробка передач',
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = 'коробка передач'
        verbose_name_plural = 'коробки передач'
        constraints = (
            models.CheckConstraint(check=Q(transmission__lenght__lte=20), name="transmission__lenght__lte"),
            models.CheckConstraint(check=Q(transmission__lenght__gte=0), name="transmission__lenght__gte")
        )


class DriveUnitType(models.Model):
    # Тип привод: полный, передний, задний
    drive_unit = models.CharField(
        verbose_name='привод',
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.drive_unit

    class Meta:
        verbose_name = 'тип привода'
        verbose_name_plural = 'типы приводов'
        constraints = (
            models.CheckConstraint(check=Q(drive_unit__lenght__lte=20), name="drive_unit__lenght__lte"),
            models.CheckConstraint(check=Q(drive_unit__lenght__gte=0), name="drive_unit__lenght__gte")
        )


class BodyTypeCar(models.Model):
    # Тип кузова: внедорожник, кабриолет, седан, купе и т.д.
    body_type = models.CharField(
        verbose_name='тип кузова',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.body_type

    class Meta:
        verbose_name = 'тип кузова'
        verbose_name_plural = 'типы кузова'
        constraints = (
            models.CheckConstraint(check=Q(body_type__lenght__lte=50), name="body_type__lenght__lte"),
            models.CheckConstraint(check=Q(body_type__lenght__gte=0), name="body_type__lenght__gte")
        )


class ColorType(models.Model):
    # Цвет кузова
    color = models.CharField(
        verbose_name='цвет',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        constraints = (
            models.CheckConstraint(check=Q(color__lenght__lte=50), name="color__lenght__lte"),
            models.CheckConstraint(check=Q(color__lenght__gte=0), name="color__lenght__gte")
        )


class AnnouncementCar(models.Model):
    # Конкретное объявление
    car_brand = models.ForeignKey(
        to="BrandCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='бренд',
    )
    car_model = models.ForeignKey(
        to="ModelCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='модель',
    )
    car_body = models.ForeignKey(
        to="BodyCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='кузов',
    )
    car_engine_type = models.ForeignKey(
        to="EngineTypeCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип двигателя',
    )
    car_transmission_type = models.ForeignKey(
        to="TransmissionType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип коробки передач',
    )
    car_drive_unit_type = models.ForeignKey(
        to="DriveUnitType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип привода',
    )
    car_body_type = models.ForeignKey(
        to="BodyTypeCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип кузова',
    )
    car_color_type = models.ForeignKey(
        to="ColorType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='цвет',
    )
    price = models.PositiveIntegerField(verbose_name='Цена')
    year_of_issue = models.PositiveIntegerField(verbose_name='Год выпуска')
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    engine_volume = models.FloatField(verbose_name='Объём двигателя')
    engine_power = models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')
    description = models.TextField(verbose_name='Описание')
    equipment = models.TextField(verbose_name='Комплектация')
    slug = models.SlugField(
        max_length=200,
        default=False,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        constraints = (
            models.CheckConstraint(check=Q(year_of_issue__lte=datetime.now().year), name="year_of_issue__lte"),
            models.CheckConstraint(check=Q(engine_volume__ge=0), name="engine_volume__ge"),
        )


class AnnouncementCarImage(models.Model):
    image = models.ImageField(
        upload_to="transport",
        db_index=True,
        verbose_name="фотографии объявлений"
    )
    announcement_car = models.ForeignKey(
        to="AnnouncementCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="",
        related_name="images"
    )