from django.contrib import admin

from .models import (
    BrandCar,
    ModelCar,
    BodyCar,
    EngineTypeCar,
    BodyTypeCar,
    ColorType,
    TransmissionType,
    DriveUnitType,
    AnnouncementCar,
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


@admin.register(EngineTypeCar)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('engine',)
    ordering = ('engine',)


@admin.register(TransmissionType)
class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('transmission',)
    ordering = ('transmission',)


@admin.register(DriveUnitType)
class DriveUnitTypeAdmin(admin.ModelAdmin):
    list_display = ('drive_unit',)
    ordering = ('drive_unit',)


@admin.register(BodyTypeCar)
class BodyTypeCarAdmin(admin.ModelAdmin):
    list_display = ('body_type',)
    ordering = ('body_type',)


@admin.register(ColorType)
class ColorTypeAdmin(admin.ModelAdmin):
    list_display = ('color',)
    ordering = ('color',)


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
            'year_of_issue',
            'mileage',
            'price',
            'car_transmission_type',
            'car_drive_unit_type'
        )
    }
