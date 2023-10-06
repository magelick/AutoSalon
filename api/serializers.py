from rest_framework.serializers import HyperlinkedModelSerializer
from transport.models import AnnouncementCar, BrandCar, ModelCar, BodyCar


class AnnouncementCarSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AnnouncementCar
        fields = '__all__'
