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
            models.CheckConstraint(check=Q(brand_name__length__lte=50), name="brand_name__length__lte"),
            models.CheckConstraint(check=Q(brand_name__length__gte=0), name="brand_name__length__gte")
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
            models.CheckConstraint(check=Q(model_name__length__lte=50), name="model_name__length__lte"),
            models.CheckConstraint(check=Q(model_name__length__gte=0), name="model_name__length__gte")
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
            models.CheckConstraint(check=Q(body_name__length__lte=50), name="body_name__length__lte"),
            models.CheckConstraint(check=Q(body_name__length__gte=0), name="body_name__length__gte")
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
            models.CheckConstraint(check=Q(engine__length__lte=20), name="engine__length__lte"),
            models.CheckConstraint(check=Q(engine__length__gte=0), name="engine__length__gte")
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
        verbose_name = 'тип коробки передач'
        verbose_name_plural = 'типы коробок передач'
        constraints = (
            models.CheckConstraint(check=Q(transmission__length__lte=20), name="transmission__length__lte"),
            models.CheckConstraint(check=Q(transmission__length__gte=0), name="transmission__length__gte")
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
            models.CheckConstraint(check=Q(drive_unit__length__lte=20), name="drive_unit__length__lte"),
            models.CheckConstraint(check=Q(drive_unit__length__gte=0), name="drive_unit__length__gte")
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
            models.CheckConstraint(check=Q(body_type__length__lte=50), name="body_type__length__lte"),
            models.CheckConstraint(check=Q(body_type__length__gte=0), name="body_type__length__gte")
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
            models.CheckConstraint(check=Q(color__length__lte=50), name="color__length__lte"),
            models.CheckConstraint(check=Q(color__length__gte=0), name="color__length__gte")
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
    slug = models.SlugField(
        max_length=200,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        constraints = (
            models.CheckConstraint(check=Q(year_of_issue__lte=datetime.now().year), name="year_of_issue__lte"),
            models.CheckConstraint(check=Q(engine_volume__gte=0), name="engine_volume__ge"),
        )


class AnnouncementCarImage(models.Model):
    image = models.ImageField(
        upload_to="transport",
        db_index=True,
        verbose_name="фотографии объявлений"
    )
    announcement_car = models.ForeignKey(
        to="AnnouncementCar",
        on_delete=models.CASCADE,
        db_index=True,
        related_name="images",
    )

    class Meta:
        verbose_name = 'фотографии автомобиля'
        verbose_name_plural = 'фотографии автомобилей'


class AnnouncementCarEquipment(models.Model):
    equipment_car = models.ForeignKey(
        to="AnnouncementCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="equipment",
        verbose_name="объявление"
    )
    climate_control_car = models.ForeignKey(
        to="ClimateControlType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="климат-контроль"
    )
    bluetooth_car = models.ForeignKey(
        to="BluetoothType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="bluetooth-система"
    )
    rain_sensor_car = models.ForeignKey(
        to="RaisSensorType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="датчик дождя",
        null=True,
        blank=True
    )
    light_sensor_car = models.ForeignKey(
        to="LightSensorType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="датчик света",
        null=True,
        blank=True
    )
    start_stop_car = models.ForeignKey(
        to="StartStopType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="start-stop система",
        null=True,
        blank=True
    )
    heated_seats_car = models.ForeignKey(
        to="HeatedSeatsType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="подогрев сидений",
        null=False,
        blank=False
    )
    ventilation_seats_car = models.ForeignKey(
        to="VentilationSeatsType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="вентиляция сидений",
        null=True,
        blank=True
    )
    adjustments_seats_car = models.ForeignKey(
        to="AdjustmentsSeatsType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="регулировка сидений"
    )
    blind_spot_monitoring_system_car = models.ForeignKey(
        to="BlindSpotMonitoringSystemType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="система контроля слепых зон",
        null=True,
        blank=True
    )
    collision_avoidance_system_car = models.ForeignKey(
        to="CollisionAvoidanceSystemType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="система избежания столкновений",
        null=True,
        blank=True
    )
    lane_departure_warning_system_car = models.ForeignKey(
        to="LaneDepartureWarningSystemType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="система предупреждения о сходе с полосы",
        null=True,
        blank=True
    )
    headlights_car = models.ForeignKey(
        to="HeadlightsType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="тип фар",
    )
    parking_sensors_car = models.ForeignKey(
        to="ParkingSensorsType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="датчики парковки",
        null=True,
        blank=True
    )
    roof_car = models.ForeignKey(
        to="RoofCarType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="тип крышы",
        null=True,
        blank=True
    )
    salon_car = models.ForeignKey(
        to="SalonCarType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="тип салона",
    )
    color_salon_car = models.ForeignKey(
        to="ColorSalonCarType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="цвет салона"
    )
    body_kit_car = models.ForeignKey(
        to="BodyKitType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name="обвес",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'комплектация'
        verbose_name_plural = 'комплектации'


class ClimateControlType(models.Model):
    climate_control_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        unique=True,
        verbose_name="климат-контроль"
    )

    def __str__(self):
        return self.climate_control_name

    class Meta:
        verbose_name = 'климат-контроль'
        verbose_name_plural = 'климат-контроли'
        constraints = (
            models.CheckConstraint(check=Q(climate_control_name__length__lte=64),
                                   name="climate_control_name__length__lte"),
            models.CheckConstraint(check=Q(climate_control_name__length__gte=0),
                                   name="climate_control_name__length__gte")
        )


class BluetoothType(models.Model):
    bluetooth_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="bluetooth-система"
    )

    def __str__(self):
        return self.bluetooth_name

    class Meta:
        verbose_name = 'bluetooth-система'
        verbose_name_plural = 'bluetooth-системы'
        constraints = (
            models.CheckConstraint(check=Q(bluetooth_name__length__lte=50), name="bluetooth_name__length__lte"),
            models.CheckConstraint(check=Q(bluetooth_name__length__gte=0), name="bluetooth_name__length__gte")
        )


class RaisSensorType(models.Model):
    rain_sensor_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="датчик дождя"
    )

    def __str__(self):
        return self.rain_sensor_name

    class Meta:
        verbose_name = 'датчик дождя'
        verbose_name_plural = 'датчики дождя'
        constraints = (
            models.CheckConstraint(check=Q(rain_sensor_name__length__lte=50), name="rain_sensor_name__length__lte"),
            models.CheckConstraint(check=Q(rain_sensor_name__length__gte=0), name="rain_sensor_name__length__gte")
        )


class LightSensorType(models.Model):
    light_sensor_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="датчик света"
    )

    def __str__(self):
        return self.light_sensor_name

    class Meta:
        verbose_name = 'датчик света'
        verbose_name_plural = 'датчики света'
        constraints = (
            models.CheckConstraint(check=Q(light_sensor_name__length__lte=50), name="light_sensor_name__length__lte"),
            models.CheckConstraint(check=Q(light_sensor_name__length__gte=0), name="light_sensor_name__length__gte")
        )


class StartStopType(models.Model):
    start_stop_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="система start-stop"
    )

    def __str__(self):
        return self.start_stop_name

    class Meta:
        verbose_name = 'система start-stop'
        verbose_name_plural = 'системы start-stop'
        constraints = (
            models.CheckConstraint(check=Q(start_stop_name__length__lte=50), name="start_stop_name__length__lte"),
            models.CheckConstraint(check=Q(start_stop_name__length__gte=0), name="start_stop_name__length__gte")
        )


class HeatedSeatsType(models.Model):
    heated_seats_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="подогрев сидений"
    )

    def __str__(self):
        return self.heated_seats_name

    class Meta:
        verbose_name = 'подогрев сидения'
        verbose_name_plural = 'подогрев сидений'
        constraints = (
            models.CheckConstraint(check=Q(heated_seats_name__length__lte=50), name="heated_seats_name__length__lte"),
            models.CheckConstraint(check=Q(heated_seats_name__length__gte=0), name="heated_seats_name__length__gte")
        )


class VentilationSeatsType(models.Model):
    ventilation_seats_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="вентиляция сидений"
    )

    def __str__(self):
        return self.ventilation_seats_name

    class Meta:
        verbose_name = 'вентиляция сидения'
        verbose_name_plural = 'вентиляция сидений'
        constraints = (
            models.CheckConstraint(check=Q(ventilation_seats_name__length__lte=50),
                                   name="ventilation_seats_name__length__lte"),
            models.CheckConstraint(check=Q(ventilation_seats_name__length__gte=0),
                                   name="ventilation_seats_name__length__gte")
        )


class AdjustmentsSeatsType(models.Model):
    adjustments_seats_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="регулировка сидений"
    )

    def __str__(self):
        return self.adjustments_seats_name

    class Meta:
        verbose_name = 'регулировка сидения'
        verbose_name_plural = 'регулировка сидений'
        constraints = (
            models.CheckConstraint(check=Q(adjustments_seats_name__length__lte=50),
                                   name="adjustments_seats_name__length__lte"),
            models.CheckConstraint(check=Q(adjustments_seats_name__length__gte=0),
                                   name="adjustments_seats_name__length__gte")
        )


class BlindSpotMonitoringSystemType(models.Model):
    blind_spot_monitoring_system_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="система контроля слепых зон"
    )

    def __str__(self):
        return self.blind_spot_monitoring_system_name

    class Meta:
        verbose_name = 'система контроля слепых зон'
        verbose_name_plural = 'системы контроля слепых зон'
        constraints = (
            models.CheckConstraint(check=Q(blind_spot_monitoring_system_name__length__lte=50),
                                   name="blind_spot_monitoring_system_name__length__lte"),
            models.CheckConstraint(check=Q(blind_spot_monitoring_system_name__length__gte=0),
                                   name="blind_spot_monitoring_system_name__length__gte")
        )


class CollisionAvoidanceSystemType(models.Model):
    collision_avoidance_system_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="система избежания столкновений"
    )

    def __str__(self):
        return self.collision_avoidance_system_name

    class Meta:
        verbose_name = 'система избежания столкновений'
        verbose_name_plural = 'системы избежания столкновений'
        constraints = (
            models.CheckConstraint(check=Q(collision_avoidance_system_name__length__lte=50),
                                   name="collision_avoidance_system_name__length__lte"),
            models.CheckConstraint(check=Q(collision_avoidance_system_name__length__gte=0),
                                   name="collision_avoidance_system_name__length__gte")
        )


class LaneDepartureWarningSystemType(models.Model):
    lane_departure_warning_system_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="система предупреждения о сходе с полосы"
    )

    def __str__(self):
        return self.lane_departure_warning_system_name

    class Meta:
        verbose_name = 'система предупреждения о сходе с полосы'
        verbose_name_plural = 'системы предупреждения о сходе с полосы'
        constraints = (
            models.CheckConstraint(check=Q(lane_departure_warning_system_name__length__lte=50),
                                   name="lane_departure_warning_system_name__length__lte"),
            models.CheckConstraint(check=Q(lane_departure_warning_system_name__length__gte=0),
                                   name="lane_departure_warning_system_name__length__gte")
        )


class HeadlightsType(models.Model):
    headlights_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="тип фар"
    )

    def __str__(self):
        return self.headlights_name

    class Meta:
        verbose_name = 'тип фар'
        verbose_name_plural = 'типы фар'
        constraints = (
            models.CheckConstraint(check=Q(headlights_name__length__lte=50), name="headlights_name__length__lte"),
            models.CheckConstraint(check=Q(headlights_name__length__gte=0), name="headlights_name__length__gte")
        )


class ParkingSensorsType(models.Model):
    parking_sensors_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="датчик парковки"
    )

    def __str__(self):
        return self.parking_sensors_name

    class Meta:
        verbose_name = 'датчик парковки'
        verbose_name_plural = 'датчики парковки'
        constraints = (
            models.CheckConstraint(check=Q(parking_sensors_name__length__lte=50),
                                   name="parking_sensors_name__length__lte"),
            models.CheckConstraint(check=Q(parking_sensors_name__length__gte=0),
                                   name="parking_sensors_name__length__gte")
        )


class RoofCarType(models.Model):
    roof_car_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="тип крышы"
    )

    def __str__(self):
        return self.roof_car_name

    class Meta:
        verbose_name = 'тип крышы'
        verbose_name_plural = 'типы крыш'
        constraints = (
            models.CheckConstraint(check=Q(roof_car_name__length__lte=50), name="roof_car_name__length__lte"),
            models.CheckConstraint(check=Q(roof_car_name__length__gte=0), name="roof_car_name__gte")
        )


class SalonCarType(models.Model):
    salon_car_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="тип салона"
    )

    def __str__(self):
        return self.salon_car_name

    class Meta:
        verbose_name = 'тип салона'
        verbose_name_plural = 'типы салона'
        constraints = (
            models.CheckConstraint(check=Q(salon_car_name__length__lte=50), name="salon_car_name__length__lte"),
            models.CheckConstraint(check=Q(salon_car_name__length__gte=0), name="salon_car_name__length__gte")
        )


class ColorSalonCarType(models.Model):
    color_salon_car_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="цвет салона"
    )

    def __str__(self):
        return self.color_salon_car_name

    class Meta:
        verbose_name = 'цвет салона'
        verbose_name_plural = 'цвета салона'
        constraints = (
            models.CheckConstraint(check=Q(color_salon_car_name__length__lte=50),
                                   name="color_salon_car_name__length__lte"),
            models.CheckConstraint(check=Q(color_salon_car_name__length__gte=0),
                                   name="color_salon_car_name__length__gte")
        )


class BodyKitType(models.Model):
    body_kit_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="обвес"
    )

    def __str__(self):
        return self.body_kit_name

    class Meta:
        verbose_name = 'обвес'
        verbose_name_plural = 'обвесы'
        constraints = (
            models.CheckConstraint(check=Q(body_kit_name__length__lte=50), name="body_kit_name__length__lte"),
            models.CheckConstraint(check=Q(body_kit_name__length__gte=0), name="body_kit_name__length__gte")
        )
