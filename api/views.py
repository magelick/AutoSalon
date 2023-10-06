from rest_framework.viewsets import ModelViewSet
from . import serializers
from transport.models import AnnouncementCar


class AnnouncementCarCreateViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()
    http_method_names = ['post']


class AnnouncementCarReadViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()
    http_method_names = ['get']


class AnnouncementCarUpdateViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()
    http_method_names = ['put']


class AnnouncementCarDeleteViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()
    http_method_names = ['delete']
