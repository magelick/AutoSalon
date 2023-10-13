from datetime import datetime
from django.db.models.functions import Length
from django.db import models
from django.db.models import Q
from django.utils.text import slugify

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
        on_delete=models.CASCADE,
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


class YearOfIssueType(models.Model):
    year_of_issue = models.PositiveIntegerField(
        verbose_name='Год выпуска',
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
        return self.slug

    class Meta:
        verbose_name = 'год выпуска'
        verbose_name_plural = 'года выпуска'
        constraints = (
            models.CheckConstraint(check=Q(year_of_issue__lte=datetime.now().year), name="year_of_issue__lte"),
        )


class MileageType(models.Model):
    mileage = models.PositiveIntegerField(
        verbose_name='Пробег',
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
        return self.slug

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'


class EngineTypeCar(models.Model):
    # Тип двигателя: бензин, дизель, электро
    engine = models.CharField(
        verbose_name='тип двигателя',
        max_length=20,
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
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
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
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
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
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
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
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
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
        verbose_name="объявление"
    )

    class Meta:
        verbose_name = 'фотографии автомобиля'
        verbose_name_plural = 'фотографии автомобилей'


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
        verbose_name='цвет кузова',
    )
    car_year_of_issue_type = models.ForeignKey(
        to="YearOfIssueType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='год выпуска'
    )
    car_mileage_type = models.ForeignKey(
        to="MileageType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='пробег'
    )
    price = models.PositiveIntegerField(verbose_name='Цена')
    engine_volume = models.FloatField(verbose_name='Объём двигателя')
    engine_power = models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        max_length=200,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.slug

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(
            f"{self.car_brand} {self.car_model} {self.car_body} {self.car_year_of_issue_type} {self.car_mileage_type} {self.price} {self.car_transmission_type} {self.car_drive_unit_type}"
        )
        super().save(self, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        constraints = (
            models.CheckConstraint(check=Q(engine_volume__gte=0), name="engine_volume__ge"),
        )


class AnnouncementCarEquipment(models.Model):
    equipment_car = models.ForeignKey(
        to="AnnouncementCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="equipment_announcement",
        verbose_name="объявление"
    )
    climate_control_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="climate_control_name_announcement",
        verbose_name="климат-контроль"
    )
    bluetooth_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="bluetooth_name_announcement",
        verbose_name="bluetooth-система"
    )
    music_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="music_system_name_announcement",
        verbose_name="aудиосистема"
    )
    rain_sensor_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="rain_sensor_name_announcement",
        verbose_name="датчик дождя"
    )
    light_sensor_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="light_sensor_name_announcement",
        verbose_name="датчик света"
    )
    start_stop_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="start_stop_name_announcement",
        verbose_name="система start-stop"
    )
    key_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="key_name_announcement",
        verbose_name="тип ключа"
    )
    door_closer_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="door_closer_name_announcement",
        verbose_name="тип ключа"
    )
    heated_seats_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="heated_seats_name_announcement",
        verbose_name="подогрев сидений"
    )
    ventilation_seats_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="ventilation_seats_name_announcement",
        verbose_name="вентиляция сидений"
    )
    adjustments_seats_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="adjustments_seats_name_announcement",
        verbose_name="регулировка сидений"
    )
    massage_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="massage_name_announcement",
        verbose_name="массаж сидений"
    )
    projection_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="projection_name_announcement",
        verbose_name="проекция"
    )
    suspension_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="suspension_name_announcement",
        verbose_name="тип подвески"
    )
    tinting_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="tinting_name_announcement",
        verbose_name="тип тонировки"
    )
    brake_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="brake_name_announcement",
        verbose_name="тип тормозов"
    )
    directional_stability_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="directional_stability_system_name_announcement",
        verbose_name="система курсовой устойчивости"
    )
    brake_assist_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="brake_assist_system_name_announcement",
        verbose_name="cистема помощи при торможении"
    )
    automatic_parking_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="automatic_parking_system_name_announcement",
        verbose_name="cистема автоматической парковки"
    )
    traffic_sign_recognition_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="traffic_sign_recognition_system_name_announcement",
        verbose_name="cистема распознования дорожных знаков"
    )
    active_lane_keeping_assist_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="active_lane_keeping_assist_name_announcement",
        verbose_name="cистема удержания в полосе"
    )
    night_vision_system_with_pedestrian_detection_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="night_vision_system_with_pedestrian_detection_name_announcement",
        verbose_name="cистема ночного видения с функцией распознавания пешеходов"
    )
    hill_start_assist_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="hill_start_assist_system_name_announcement",
        verbose_name="cистема помощи при старте в гору"
    )
    blind_spot_monitoring_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="blind_spot_monitoring_system_name_announcement",
        verbose_name="система контроля слепых зон"
    )
    collision_avoidance_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="collision_avoidance_system_name_announcement",
        verbose_name="система избежания столкновений"
    )
    lane_departure_warning_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="lane_departure_warning_system_name_announcement",
        verbose_name="система предупреждения о сходе с полосы"
    )
    wireless_charging_for_smartphone_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="wireless_charging_for_smartphone_name_announcement",
        verbose_name="беспроводная зарядка для смартфона"
    )
    contactless_trunk_opening_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="contactless_trunk_opening_name_announcement",
        verbose_name="бесконтактное открытие багажника"
    )
    electric_trunk_lid_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="electric_trunk_lid_name_announcement",
        verbose_name="электропривод крышки багажника"
    )
    remote_engine_start_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="remote_engine_start_name_announcement",
        verbose_name="дистанционный запуск двигателя"
    )
    remote_control_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="remote_control_car_name_announcement",
        verbose_name="дистанционное управление автомобилем"
    )
    navigation_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="navigation_name_announcement",
        verbose_name="дистанционное управление автомобилем"
    )
    headlights_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="headlights_name_announcement",
        verbose_name="тип фар"
    )
    parking_sensors_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="parking_sensors_name_announcement",
        verbose_name="датчик парковки"
    )
    cameras_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="cameras_system_name_announcement",
        verbose_name="тип камеры"
    )
    interior_lighting_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="interior_lighting_name_announcement",
        verbose_name="подсветка салона"
    )
    roof_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="roof_car_name_announcement",
        verbose_name="тип крыши"
    )
    seat_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="seat_name_announcement",
        verbose_name="тип сидений"
    )
    salon_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="salon_car_name_announcement",
        verbose_name="тип салона"
    )
    color_salon_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="color_salon_car_name_announcement",
        verbose_name="цвет салона"
    )
    body_kit_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="body_kit_name_announcement",
        verbose_name="обвес"
    )

    class Meta:
        verbose_name = 'комплектация'
        verbose_name_plural = 'комплектации'


class EquipmentCar(models.Model):
    characteristic = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        unique=True,
        verbose_name="характеристика комплектации"
    )

    def __str__(self):
        return self.characteristic

    class Meta:
        verbose_name = 'характеристика коплектации'
        verbose_name_plural = 'характеристики комплектации'
        constraints = (
            models.CheckConstraint(check=Q(characteristic__length__lte=64),
                                   name="characteristic__length__lte"),
            models.CheckConstraint(check=Q(characteristic__length__gte=0),
                                   name="characteristic__length__gte")
        )
