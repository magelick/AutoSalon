from rest_framework.serializers import HyperlinkedModelSerializer

from ..transport.models import AnnouncementCar


class AnnouncementCarSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AnnouncementCar
        fields = '__all__'


