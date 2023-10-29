from rest_framework.routers import DefaultRouter
from .views import (
    AnnouncementCarAPIViewSet,
    BrandCarAPIViewSet,
    ModelCarAPIViewSet,
    BodyCarAPIViewSet,
    MileageTypeAPIViewSet,
    YearOfIssueTypeAPIViewSet,
    EngineTypeCarAPIViewSet,
    TransmissionTypeAPIViewSet,
    DriveUnitTypeAPIViewSet,
    BodyTypeCarAPIViewSet,
    ColorTypeAPIViewSet,
    AnnouncementCarEquipmentAPIViewSet,
    EquipmentCarAPIViewSet
)
from django.urls import path, include

# Инициализируем роутер
router = DefaultRouter()


# Добавляем ручки в URL
router.register("cars", AnnouncementCarAPIViewSet, basename="announcement_car")
router.register("brands", BrandCarAPIViewSet, basename="brand_car")
router.register("models", ModelCarAPIViewSet, basename="model_car")
router.register("bodies", BodyCarAPIViewSet, basename="body_car")
router.register("mileages", MileageTypeAPIViewSet, basename="mileage")
router.register("years_of_issue", YearOfIssueTypeAPIViewSet, basename="year_of_issue")
router.register("engines", EngineTypeCarAPIViewSet, basename="engine_type")
router.register("drive_units", DriveUnitTypeAPIViewSet, basename="drive_unit")
router.register("transmissions", TransmissionTypeAPIViewSet, basename="transmission")
router.register("body_types", BodyTypeCarAPIViewSet, basename="body_type")
router.register("colors", ColorTypeAPIViewSet, basename="color")
router.register("announcement_equipments", AnnouncementCarEquipmentAPIViewSet, basename="announcement_equipment")
router.register("equipments", EquipmentCarAPIViewSet, basename="equipment")


# Версия API
urlpatterns = [
    path("v1/", include(router.urls))
]