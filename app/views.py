from rest_framework.viewsets import ModelViewSet

from ..transport.models import AnnouncementCar
from .serializers import AnnouncementCarSerializer


class AnnouncementCarApiView(ModelViewSet):
    queryset = AnnouncementCar.objects.all()
    serializer_class = AnnouncementCarSerializer
    http_method_names = ['get']
