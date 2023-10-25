from datetime import datetime
from django.db.models.functions import Length
from django.db import models
from django.db.models import Q
from django.utils.text import slugify

models.CharField.register_class_lookup(Length)


class BrandCar(models.Model):
    """
    Модель Бренд (марка): Volkswagen
    """
    # Бренд
    brand_name = models.CharField(
        verbose_name='марка',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг бренда
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.brand_name

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'
        constraints = (
            models.CheckConstraint(check=Q(brand_name__length__lte=50), name="brand_name__length__lte"),
            models.CheckConstraint(check=Q(brand_name__length__gte=0), name="brand_name__length__gte")
        )


class ModelCar(models.Model):
    """
    Модель Марки: Passat
    """
    # Модель бренда
    model_name = models.CharField(
        verbose_name='модель',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг модели
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    # Ссылка на конкретный бренд
    brand = models.ForeignKey(
        to="BrandCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="models"
    )

    def __str__(self):
        return self.model_name

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'модель'
        verbose_name_plural = 'модели'
        constraints = (
            models.CheckConstraint(check=Q(model_name__length__lte=50), name="model_name__length__lte"),
            models.CheckConstraint(check=Q(model_name__length__gte=0), name="model_name__length__gte")
        )


class BodyCar(models.Model):
    """
    Модель Кузова: B3 и B8
    """
    # Кузов модели
    body_name = models.CharField(
        verbose_name='кузов',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг кузова
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    # Ссылка на кокнертную  модель
    model = models.ForeignKey(
        to='ModelCar',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='bodies'
    )

    def __str__(self):
        return self.body_name

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'кузов'
        verbose_name_plural = 'кузова'
        constraints = (
            models.CheckConstraint(check=Q(body_name__length__lte=50), name="body_name__length__lte"),
            models.CheckConstraint(check=Q(body_name__length__gte=0), name="body_name__length__gte")
        )


class YearOfIssueType(models.Model):
    """
    Модель Года выпуска
    """
    # Год выпуска
    year_of_issue = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        null=False,
        blank=False,
        unique=True
    )
    # Слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.slug

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'год выпуска'
        verbose_name_plural = 'года выпуска'
        constraints = (
            models.CheckConstraint(check=Q(year_of_issue__lte=datetime.now().year), name="year_of_issue__lte"),
        )


class MileageType(models.Model):
    """
    Модель Пробега
    """
    # Пробег
    mileage = models.PositiveIntegerField(
        verbose_name='Пробег',
        null=False,
        blank=False,
        unique=True
    )
    # Слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.slug

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'


class EngineTypeCar(models.Model):
    """
    Модель типа двигателя:
    """
    # Тип двигателя
    engine = models.CharField(
        verbose_name='тип двигателя',
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.engine

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'тип двигателя'
        verbose_name_plural = 'типы двигателей'
        constraints = (
            models.CheckConstraint(check=Q(engine__length__lte=20), name="engine__length__lte"),
            models.CheckConstraint(check=Q(engine__length__gte=0), name="engine__length__gte")
        )


class TransmissionType(models.Model):
    """
    Модель типа коробки передач
    """
    # Тип коробки передач
    transmission = models.CharField(
        verbose_name='коробка передач',
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    # слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.transmission

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'тип коробки передач'
        verbose_name_plural = 'типы коробок передач'
        constraints = (
            models.CheckConstraint(check=Q(transmission__length__lte=20), name="transmission__length__lte"),
            models.CheckConstraint(check=Q(transmission__length__gte=0), name="transmission__length__gte")
        )


class DriveUnitType(models.Model):
    """
    Модель типа привода
    """
    # Тип привода
    drive_unit = models.CharField(
        verbose_name='привод',
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.drive_unit

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'тип привода'
        verbose_name_plural = 'типы приводов'
        constraints = (
            models.CheckConstraint(check=Q(drive_unit__length__lte=20), name="drive_unit__length__lte"),
            models.CheckConstraint(check=Q(drive_unit__length__gte=0), name="drive_unit__length__gte")
        )


class BodyTypeCar(models.Model):
    """
    Модель типа кузова
    """
    # Тип кузова
    body_type = models.CharField(
        verbose_name='тип кузова',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.body_type

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'тип кузова'
        verbose_name_plural = 'типы кузова'
        constraints = (
            models.CheckConstraint(check=Q(body_type__length__lte=50), name="body_type__length__lte"),
            models.CheckConstraint(check=Q(body_type__length__gte=0), name="body_type__length__gte")
        )


class ColorType(models.Model):
    """
    Модель цвета кузова
    """
    # Цвет кузова
    color = models.CharField(
        verbose_name='цвет',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    # Слаг
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.color

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        constraints = (
            models.CheckConstraint(check=Q(color__length__lte=50), name="color__length__lte"),
            models.CheckConstraint(check=Q(color__length__gte=0), name="color__length__gte")
        )


class AnnouncementCarImage(models.Model):
    """
    Модель фотографий конкретного объявления
    """
    # Фотографии
    image = models.ImageField(
        upload_to="transport",
        db_index=True,
        verbose_name="фотографии объявлений"
    )
    # Ссылка на конкретное объявление
    announcement_car = models.ForeignKey(
        to="AnnouncementCar",
        on_delete=models.CASCADE,
        db_index=True,
        related_name="images",
        verbose_name="объявление"
    )

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'фотографии автомобиля'
        verbose_name_plural = 'фотографии автомобилей'


class AnnouncementCar(models.Model):
    """
    Модель конкретного объявление
    """
    # Ссылка на бренд автомобиля
    car_brand = models.ForeignKey(
        to="BrandCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='бренд',
    )
    # Ссылка на модель бренда
    car_model = models.ForeignKey(
        to="ModelCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='модель',
    )
    # Ссылка на кузова модели
    car_body = models.ForeignKey(
        to="BodyCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='кузов',
    )
    # Ссылка на тип двигателя
    car_engine_type = models.ForeignKey(
        to="EngineTypeCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип двигателя',
    )
    # Ссылка на тип коробки передач
    car_transmission_type = models.ForeignKey(
        to="TransmissionType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип коробки передач',
    )
    # Ссылка на ти привода
    car_drive_unit_type = models.ForeignKey(
        to="DriveUnitType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип привода',
    )
    # Ссылка на тип кузова
    car_body_type = models.ForeignKey(
        to="BodyTypeCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='тип кузова',
    )
    # Ссылка на цвет кузова
    car_color_type = models.ForeignKey(
        to="ColorType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='цвет кузова',
    )
    # Ссылка на год выпуска
    car_year_of_issue_type = models.ForeignKey(
        to="YearOfIssueType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='год выпуска'
    )
    # Ссылка на пробег
    car_mileage_type = models.ForeignKey(
        to="MileageType",
        on_delete=models.DO_NOTHING,
        db_index=True,
        verbose_name='пробег'
    )
    price = models.PositiveIntegerField(verbose_name='Цена')  # Цена кокнретного объявления
    engine_volume = models.FloatField(verbose_name='Объём двигателя')  # Объём двигателя
    engine_power = models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')  # Мощность двигателя (л/с)
    description = models.TextField(verbose_name='Описание')  # Описания кокретного объявления
    slug = models.SlugField(  # Слаг
        max_length=200,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.slug

    # Функция, генерирующая слаг конкретного объявления
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(
            f"{self.car_brand} {self.car_model} {self.car_body} {self.car_year_of_issue_type} {self.car_mileage_type} {self.price} {self.car_transmission_type} {self.car_drive_unit_type}"
        )
        super().save(self, force_update=False, using=None, update_fields=None)

    class Meta:
        """
        Настройки модели
        """
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        constraints = (
            models.CheckConstraint(check=Q(engine_volume__gte=0), name="engine_volume__ge"),
        )


class AnnouncementCarEquipment(models.Model):
    """
    Модель компелктации конкертного объявления
    """
    # Ссылка на конкретное объявления
    equipment_car = models.ForeignKey(
        to="AnnouncementCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        related_name="equipment_announcement",
        verbose_name="объявление"
    )
    # Климат-контроль
    climate_control_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="climate_control_name_announcement",
        verbose_name="климат-контроль"
    )
    # Bluetooth-система
    bluetooth_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="bluetooth_name_announcement",
        verbose_name="bluetooth-система"
    )
    # Аудиосистема
    music_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="music_system_name_announcement",
        verbose_name="aудиосистема"
    )
    # Датчик дождя
    rain_sensor_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="rain_sensor_name_announcement",
        verbose_name="датчик дождя"
    )
    # Датчик света
    light_sensor_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="light_sensor_name_announcement",
        verbose_name="датчик света"
    )
    # Система start-
    start_stop_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="start_stop_name_announcement",
        verbose_name="система start-stop"
    )
    # Тип ключа
    key_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="key_name_announcement",
        verbose_name="тип ключа"
    )
    # Доводчики дверей
    door_closer_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="door_closer_name_announcement",
        verbose_name="доводчики дверей"
    )
    # Подогрев сидений
    heated_seats_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="heated_seats_name_announcement",
        verbose_name="подогрев сидений"
    )
    # Вентиляция сидений
    ventilation_seats_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="ventilation_seats_name_announcement",
        verbose_name="вентиляция сидений"
    )
    # Регулировка сидений
    adjustments_seats_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="adjustments_seats_name_announcement",
        verbose_name="регулировка сидений"
    )
    # Массаж сидений
    massage_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="massage_name_announcement",
        verbose_name="массаж сидений"
    )
    # Проекция
    projection_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="projection_name_announcement",
        verbose_name="проекция"
    )
    # Тип подвески
    suspension_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="suspension_name_announcement",
        verbose_name="тип подвески"
    )
    # Тип тонировки
    tinting_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="tinting_name_announcement",
        verbose_name="тип тонировки"
    )
    # Тип тормозов
    brake_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="brake_name_announcement",
        verbose_name="тип тормозов"
    )
    # Система курсовой устойчивости
    directional_stability_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="directional_stability_system_name_announcement",
        verbose_name="система курсовой устойчивости"
    )
    # cистема помощи при торможении
    brake_assist_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="brake_assist_system_name_announcement",
        verbose_name="cистема помощи при торможении"
    )
    # cистема автоматической парковки
    automatic_parking_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="automatic_parking_system_name_announcement",
        verbose_name="cистема автоматической парковки"
    )
    # cистема распознования дорожных знаков
    traffic_sign_recognition_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="traffic_sign_recognition_system_name_announcement",
        verbose_name="cистема распознования дорожных знаков"
    )
    # cистема удержания в полосе
    active_lane_keeping_assist_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="active_lane_keeping_assist_name_announcement",
        verbose_name="cистема удержания в полосе"
    )
    # cистема ночного видения с функцией распознавания пешеходов
    night_vision_system_with_pedestrian_detection_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="night_vision_system_with_pedestrian_detection_name_announcement",
        verbose_name="cистема ночного видения с функцией распознавания пешеходов"
    )
    # cистема помощи при старте в гору
    hill_start_assist_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="hill_start_assist_system_name_announcement",
        verbose_name="cистема помощи при старте в гору"
    )
    # система контроля слепых зон
    blind_spot_monitoring_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="blind_spot_monitoring_system_name_announcement",
        verbose_name="система контроля слепых зон"
    )
    # система избежания столкновений
    collision_avoidance_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="collision_avoidance_system_name_announcement",
        verbose_name="система избежания столкновений"
    )
    # система предупреждения о сходе с полосы
    lane_departure_warning_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="lane_departure_warning_system_name_announcement",
        verbose_name="система предупреждения о сходе с полосы"
    )
    # беспроводная зарядка для смартфона
    wireless_charging_for_smartphone_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="wireless_charging_for_smartphone_name_announcement",
        verbose_name="беспроводная зарядка для смартфона"
    )
    # бесконтактное открытие багажника
    contactless_trunk_opening_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="contactless_trunk_opening_name_announcement",
        verbose_name="бесконтактное открытие багажника"
    )
    # электропривод крышки багажника
    electric_trunk_lid_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="electric_trunk_lid_name_announcement",
        verbose_name="электропривод крышки багажника"
    )
    # дистанционный запуск двигателя
    remote_engine_start_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="remote_engine_start_name_announcement",
        verbose_name="дистанционный запуск двигателя"
    )
    # дистанционное управление автомобилем
    remote_control_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="remote_control_car_name_announcement",
        verbose_name="дистанционное управление автомобилем"
    )
    # навигацонная система
    navigation_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="navigation_name_announcement",
        verbose_name="навигацонная система"
    )
    # тип фар
    headlights_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="headlights_name_announcement",
        verbose_name="тип фар"
    )
    # датчик парковки
    parking_sensors_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="parking_sensors_name_announcement",
        verbose_name="датчик парковки"
    )
    # тип камеры
    cameras_system_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="cameras_system_name_announcement",
        verbose_name="тип камеры"
    )
    # подсветка салона
    interior_lighting_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="interior_lighting_name_announcement",
        verbose_name="подсветка салона"
    )
    # тип крыши
    roof_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="roof_car_name_announcement",
        verbose_name="тип крыши"
    )
    # тип сидений
    seat_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="seat_name_announcement",
        verbose_name="тип сидений"
    )
    # тип салона
    salon_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="salon_car_name_announcement",
        verbose_name="тип салона"
    )
    # цвет салона
    color_salon_car_name = models.ForeignKey(
        to="EquipmentCar",
        on_delete=models.DO_NOTHING,
        db_index=True,
        null=True,
        blank=True,
        related_name="color_salon_car_name_announcement",
        verbose_name="цвет салона"
    )
    # обвес
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
        """
        Настройки модели
        """
        verbose_name = 'комплектация'
        verbose_name_plural = 'комплектации'


class EquipmentCar(models.Model):
    """
    Модель хаарктеристик компелктации кокретного объявления
    """
    # Характеристика
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
        """
        Настройки модели
        """
        verbose_name = 'характеристика коплектации'
        verbose_name_plural = 'характеристики комплектации'
        constraints = (
            models.CheckConstraint(check=Q(characteristic__length__lte=64),
                                   name="characteristic__length__lte"),
            models.CheckConstraint(check=Q(characteristic__length__gte=0),
                                   name="characteristic__length__gte")
        )
