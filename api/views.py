from rest_framework.viewsets import ModelViewSet
from . import serializers
from transport.models import AnnouncementCar
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView


class AnnouncementCarCreateViewSet(ModelViewSet):
    queryset = AnnouncementCar.objects.all()
    serializer_class = serializers.AnnouncementCarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

