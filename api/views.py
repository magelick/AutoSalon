from rest_framework.viewsets import ModelViewSet
from . import serializers
from transport.models import AnnouncementCar
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView


class AnnouncementCarCreateViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()


class AnnouncementCarReadViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()


class AnnouncementCarUpdateViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()


class AnnouncementCarDeleteViewSet(ModelViewSet):
    serializer_class = serializers.AnnouncementCarSerializer
    queryset = AnnouncementCar.objects.all()
