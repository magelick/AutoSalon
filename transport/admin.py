from django.contrib import admin

from .models import (
    BrandCar,
    ModelCar,
    BodyCar,
    Description,
    EngineType,
    BodyTypeCar,
    ColorType,
    TransmissionType,
    DriveUnitType,
    AnnouncementCar
)


@admin.register(BrandCar)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('brand',)
    prepopulated_fields = {
        'slug': ('brand',)
    }
    ordering = ('brand',)


@admin.register(ModelCar)
class ModelAdmin(admin.ModelAdmin):
    search_fields = ('model',)
    list_display = ('model', 'brand')
    prepopulated_fields = {
        'slug': ('model',)
    }
    ordering = ('brand',)


@admin.register(BodyCar)
class BodyAdmin(admin.ModelAdmin):
    search_fields = ('body',)
    list_display = ('body', 'model')
    prepopulated_fields = {
        'slug': ('body',)
    }
    ordering = ('model',)


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    search_fields = ('price', 'year_of_issue', 'mileage')
    list_display = ('body', 'year_of_issue', 'price', 'mileage')
    list_filter = ('body', 'year_of_issue', 'price', 'mileage')
    ordering = ('body',)


@admin.register(EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('engine_type',)
    ordering = ('engine_type',)


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
    list_display = ('type_body',)
    ordering = ('type_body',)


@admin.register(ColorType)
class ColorTypeAdmin(admin.ModelAdmin):
    search_fields = ('color',)
    list_display = ('color',)
    ordering = ('color',)


@admin.register(AnnouncementCar)
class AnnouncementCarAdmin(admin.ModelAdmin):
    search_fields = ('car_brand', 'car_model', 'car_body')
    list_display = ('car_brand',
                    'car_model',
                    'car_body',
                    'car_engine_type',
                    'car_transmission_type',
                    'car_drive_unit_type'
                    )
    ordering = ('car_brand', 'car_model', 'car_body')
