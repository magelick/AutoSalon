from rest_framework.viewsets import ModelViewSet
from . import serializers
from transport.models import AnnouncementCar
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView


class AnnouncementCarCreateViewSet(ModelViewSet):
    queryset = AnnouncementCar.objects.all()
    serializer_class = serializers.AnnouncementCarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

# class AnnouncementCarReadViewSet(ModelViewSet):
#     def get(self, request):
#         return self.list(
#             request,
#             queryset=AnnouncementCar.objects.all(),
#             serializers=serializers.AnnouncementCarSerializer
#         )
#
#
# class AnnouncementCarUpdateViewSet(ModelViewSet):
#     def put(self, request):
#         return self.update(
#             request,
#             queryset=AnnouncementCar.objects.all(),
#             serializers=serializers.AnnouncementCarSerializer
#         )
#
#
# class AnnouncementCarDeleteViewSet(ModelViewSet):
#     def delete(self, request):
#         return self.destroy(
#             request,
#             queryset=AnnouncementCar.objects.all(),
#             serializers=serializers.AnnouncementCarSerializer
#         )
