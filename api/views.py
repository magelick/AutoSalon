from rest_framework.viewsets import ModelViewSet
from . import serializers
from transport.models import (
    AnnouncementCar,
    BrandCar,
    ModelCar,
    BodyCar,
    YearOfIssueType,
    MileageType,
    EngineTypeCar,
    TransmissionType,
    DriveUnitType,
    BodyTypeCar,
    ColorType,
    AnnouncementCarEquipment,
    EquipmentCar
)


class AnnouncementCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Объявления
    """
    queryset = AnnouncementCar.objects.all()
    serializer_class = serializers.AnnouncementCarSerializer


class BrandCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Бренда
    """
    queryset = BrandCar.objects.all()
    serializer_class = serializers.BrandCarSerializer


class ModelCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Модели бренда
    """
    queryset = ModelCar.objects.all()
    serializer_class = serializers.ModelCarSerializer


class BodyCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Кузова модели
    """
    queryset = BodyCar.objects.all()
    serializer_class = serializers.BodyCarSerializer


class YearOfIssueTypeAPIViewSet(ModelViewSet):
    """
    Ручка для модели Года выпуска
    """
    queryset = YearOfIssueType.objects.all()
    serializer_class = serializers.YearOfIssueTypeSerializer


class MileageTypeAPIViewSet(ModelViewSet):
    """
    Ручка для модели Пробега
    """
    queryset = MileageType.objects.all()
    serializer_class = serializers.MileageTypeSerializer


class EngineTypeCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Типа двигателя
    """
    queryset = EngineTypeCar.objects.all()
    serializer_class = serializers.EngineTypeCarSerializer


class TransmissionTypeAPIViewSet(ModelViewSet):
    """
    Ручка для модели Типа коробки передач
    """
    queryset = TransmissionType.objects.all()
    serializer_class = serializers.TransmissionTypeSerializer


class DriveUnitTypeAPIViewSet(ModelViewSet):
    """
    Ручка для модели Типа привода
    """
    queryset = DriveUnitType.objects.all()
    serializer_class = serializers.DriveUnitTypeSerializer


class BodyTypeCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Типа кузова
    """
    queryset = BodyTypeCar.objects.all()
    serializer_class = serializers.BodyTypeCarSerializer


class ColorTypeAPIViewSet(ModelViewSet):
    """
    Ручка для модели Цвета кузова
    """
    queryset = ColorType.objects.all()
    serializer_class = serializers.ColorTypeSerializer


class AnnouncementCarEquipmentAPIViewSet(ModelViewSet):
    """
    Ручка для модели Комплектации конкретного объявления
    """
    queryset = AnnouncementCarEquipment.objects.all()
    serializer_class = serializers.AnnouncementCarEquipmentSerializer


class EquipmentCarAPIViewSet(ModelViewSet):
    """
    Ручка для модели Характеристик комплектации
    """
    queryset = EquipmentCar.objects.all()
    serializer_class = serializers.EquipmentCarSerializer
