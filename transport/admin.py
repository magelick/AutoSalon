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
    AnnouncementCarImage,
    AnnouncementCarEquipment,
    ClimateControlType,
    BluetoothType,
    HeadlightsType,
    RoofCarType,
    SalonCarType,
    BodyKitType,
    RaisSensorType,
    ParkingSensorsType,
    StartStopType,
    HeatedSeatsType,
    LightSensorType,
    AdjustmentsSeatsType,
    VentilationSeatsType,
    ColorSalonCarType,
    CollisionAvoidanceSystemType,
    BlindSpotMonitoringSystemType,
    LaneDepartureWarningSystemType
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


@admin.register(AnnouncementCarImage)
class AnnouncementCarImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    ordering = ('announcement_car',)


@admin.register(AnnouncementCarEquipment)
class AnnouncementCarEquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'equipment_car',
        'climate_control_car',
        'bluetooth_car',
        'rain_sensor_car',
        'light_sensor_car',
        'start_stop_car',
        'heated_seats_car',
        'ventilation_seats_car',
        'adjustments_seats_car',
        'blind_spot_monitoring_system_car',
        'collision_avoidance_system_car',
        'lane_departure_warning_system_car',
        'headlights_car',
        'parking_sensors_car',
        'roof_car',
        'salon_car',
        'color_salon_car',
        'body_kit_car'
    )
    ordering = ('equipment_car',)


@admin.register(ClimateControlType)
class ClimateControlTypeAdmin(admin.ModelAdmin):
    list_display = ('climate_control_name',)
    ordering = ('climate_control_name',)


@admin.register(BluetoothType)
class BluetoothTypeAdmin(admin.ModelAdmin):
    list_display = ('bluetooth_name',)
    ordering = ('bluetooth_name',)


@admin.register(RaisSensorType)
class RaisSensorTypeAdmin(admin.ModelAdmin):
    list_display = ('rain_sensor_name',)
    ordering = ('rain_sensor_name',)


@admin.register(LightSensorType)
class LightSensorTypeAdmin(admin.ModelAdmin):
    list_display = ('light_sensor_name',)
    ordering = ('light_sensor_name',)


@admin.register(StartStopType)
class StartStopTypeAdmin(admin.ModelAdmin):
    list_display = ('start_stop_name',)
    ordering = ('start_stop_name',)


@admin.register(HeatedSeatsType)
class HeatedSeatsTypeAdmin(admin.ModelAdmin):
    list_display = ('heated_seats_name',)
    ordering = ('heated_seats_name',)


@admin.register(VentilationSeatsType)
class VentilationSeatsTypeAdmin(admin.ModelAdmin):
    list_display = ('ventilation_seats_name',)
    ordering = ('ventilation_seats_name',)


@admin.register(AdjustmentsSeatsType)
class AdjustmentsSeatsTypeAdmin(admin.ModelAdmin):
    list_display = ('adjustments_seats_name',)
    ordering = ('adjustments_seats_name',)


@admin.register(BlindSpotMonitoringSystemType)
class BlindSpotMonitoringSystemTypeAdmin(admin.ModelAdmin):
    list_display = ('blind_spot_monitoring_system_name',)
    ordering = ('blind_spot_monitoring_system_name',)


@admin.register(CollisionAvoidanceSystemType)
class CollisionAvoidanceSystemTypeAdmin(admin.ModelAdmin):
    list_display = ('collision_avoidance_system_name',)
    ordering = ('collision_avoidance_system_name',)


@admin.register(LaneDepartureWarningSystemType)
class LaneDepartureWarningSystemTypeAdmin(admin.ModelAdmin):
    list_display = ('lane_departure_warning_system_name',)
    ordering = ('lane_departure_warning_system_name',)


@admin.register(HeadlightsType)
class HeadlightsTypeAdmin(admin.ModelAdmin):
    list_display = ('headlights_name',)
    ordering = ('headlights_name',)


@admin.register(ParkingSensorsType)
class ParkingSensorsTypeAdmin(admin.ModelAdmin):
    list_display = ('parking_sensors_name',)
    ordering = ('parking_sensors_name',)


@admin.register(RoofCarType)
class RoofCarTypeAdmin(admin.ModelAdmin):
    list_display = ('roof_car_name',)
    ordering = ('roof_car_name',)


@admin.register(SalonCarType)
class SalonCarTypeAdmin(admin.ModelAdmin):
    list_display = ('salon_car_name',)
    ordering = ('salon_car_name',)


@admin.register(ColorSalonCarType)
class ColorSalonCarTypeAdmin(admin.ModelAdmin):
    list_display = ('color_salon_car_name',)
    ordering = ('color_salon_car_name',)


@admin.register(BodyKitType)
class BodyKitTypeAdmin(admin.ModelAdmin):
    list_display = ('body_kit_name',)
    ordering = ('body_kit_name',)
