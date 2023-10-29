from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer
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


class AnnouncementCarSerializer(ModelSerializer):
    """
    Сериализатор модели Объявления
    """
    class Meta:
        model = AnnouncementCar
        fields = '__all__'


class BrandCarSerializer(ModelSerializer):
    """
    Сериализатор омдели Бренда
    """
    class Meta:
        model = BrandCar
        fields = '__all__'


class ModelCarSerializer(ModelSerializer):
    """
    Сериализатор модели Модели бренда
    """
    class Meta:
        model = ModelCar
        fields = '__all__'


class BodyCarSerializer(ModelSerializer):
    """
    Сериализатор модель Кузова
    """
    class Meta:
        model = BodyCar
        fields = '__all__'


class YearOfIssueTypeSerializer(ModelSerializer):
    """
    Сериализатор модель Года выпуска
    """
    class Meta:
        model = YearOfIssueType
        fields = '__all__'


class MileageTypeSerializer(ModelSerializer):
    """
    Сериализатор модель Пробега
    """
    class Meta:
        model = MileageType
        fields = '__all__'


class EngineTypeCarSerializer(ModelSerializer):
    """
    Сериализатор модели Типа двигателя
    """
    class Meta:
        model = EngineTypeCar
        fields = '__all__'


class TransmissionTypeSerializer(ModelSerializer):
    """
    Сериализатор модели Типа коробки передач
    """
    class Meta:
        model = TransmissionType
        fields = '__all__'


class DriveUnitTypeSerializer(ModelSerializer):
    """
    Сериализатор модели Тип привода
    """
    class Meta:
        model = DriveUnitType
        fields = '__all__'


class ColorTypeSerializer(ModelSerializer):
    """
    Сериализатор модели Цвета кузова
    """
    class Meta:
        model = ColorType
        fields = '__all__'


class BodyTypeCarSerializer(ModelSerializer):
    """
    Сериализатор модели Тип кузова
    """
    class Meta:
        model = BodyTypeCar
        fields = '__all__'


class AnnouncementCarEquipmentSerializer(ModelSerializer):
    """
    Сериализатор модели Комплектации определённого объявления
    """
    class Meta:
        model = AnnouncementCarEquipment
        fields = '__all__'


class EquipmentCarSerializer(ModelSerializer):
    """
    Сериализатор модели Характеристик комплектации
    """
    class Meta:
        model = EquipmentCar
        fields = '__all__'