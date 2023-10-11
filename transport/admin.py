from django.contrib import admin
from django.utils.text import slugify

from .models import (
    BrandCar,
    ModelCar,
    BodyCar,
    YearOfIssueType,
    MileageType,
    EngineTypeCar,
    BodyTypeCar,
    ColorType,
    TransmissionType,
    DriveUnitType,
    AnnouncementCar,
    AnnouncementCarImage,
    AnnouncementCarEquipment,
    EquipmentCar
)


@admin.register(BrandCar)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('brand_name',)
    prepopulated_fields = {
        'slug': ('brand_name',)
    }
    ordering = ('brand_name',)


@admin.register(ModelCar)
class ModelAdmin(admin.ModelAdmin):
    search_fields = ('model_name',)
    list_display = ('model_name', 'brand')
    prepopulated_fields = {
        'slug': ('model_name',)
    }
    ordering = ('brand',)


@admin.register(BodyCar)
class BodyAdmin(admin.ModelAdmin):
    search_fields = ('body_name',)
    list_display = ('body_name', 'model')
    prepopulated_fields = {
        'slug': ('body_name',)
    }
    ordering = ('model',)


@admin.register(YearOfIssueType)
class YYearOfIssueTypeAdmin(admin.ModelAdmin):
    list_display = ('year_of_issue',)
    ordering = ('year_of_issue',)
    prepopulated_fields = {
        'slug': ('year_of_issue',)
    }


@admin.register(MileageType)
class MileageTypeAdmin(admin.ModelAdmin):
    list_display = ('mileage',)
    ordering = ('mileage',)
    prepopulated_fields = {
        'slug': ('mileage',)
    }


@admin.register(EngineTypeCar)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('engine',)
    ordering = ('engine',)
    prepopulated_fields = {
        'slug': ('engine',)
    }


@admin.register(TransmissionType)
class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('transmission',)
    ordering = ('transmission',)
    prepopulated_fields = {
        'slug': ('transmission',)
    }


@admin.register(DriveUnitType)
class DriveUnitTypeAdmin(admin.ModelAdmin):
    list_display = ('drive_unit',)
    ordering = ('drive_unit',)
    prepopulated_fields = {
        'slug': ('drive_unit',)
    }


@admin.register(BodyTypeCar)
class BodyTypeCarAdmin(admin.ModelAdmin):
    list_display = ('body_type',)
    ordering = ('body_type',)
    prepopulated_fields = {
        'slug': ('body_type',)
    }


@admin.register(ColorType)
class ColorTypeAdmin(admin.ModelAdmin):
    list_display = ('color',)
    ordering = ('color',)
    prepopulated_fields = {
        'slug': ('color',)
    }


@admin.register(AnnouncementCar)
class AnnouncementCarAdmin(admin.ModelAdmin):
    search_fields = ('car_brand', 'car_model', 'car_body')
    list_display = (
        'car_brand',
        'car_model',
        'car_body',
        'car_engine_type',
        'car_transmission_type',
        'car_drive_unit_type'
    )
    ordering = ('car_brand', 'car_model', 'car_body')
    prepopulated_fields = {
        'slug': (
            'car_brand',
            'car_model',
            'car_body',
            'car_year_of_issue_type',
            'car_mileage_type',
            'price',
            'car_transmission_type',
            'car_drive_unit_type'
        )
    }


@admin.register(AnnouncementCarImage)
class AnnouncementCarImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    ordering = ('announcement_car',)


@admin.register(AnnouncementCarEquipment)
class AnnouncementCarEquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'equipment_car',
        'climate_control_name',
        'bluetooth_name',
        'music_system_name',
        'rain_sensor_name',
        'light_sensor_name',
        'start_stop_name',
        'heated_seats_name',
        'ventilation_seats_name',
        'adjustments_seats_name',
        'blind_spot_monitoring_system_name',
        'collision_avoidance_system_name',
        'lane_departure_warning_system_name',
        'headlights_name',
        'parking_sensors_name',
        'roof_car_name',
        'salon_car_name',
        'color_salon_car_name',
        'body_kit_name'
    )
    ordering = ('equipment_car',)


@admin.register(EquipmentCar)
class EquipmentCarAdmin(admin.ModelAdmin):
    list_display = ('characteristic',)
    ordering = ('characteristic',)
