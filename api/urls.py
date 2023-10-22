from rest_framework.routers import SimpleRouter
from api.views import AnnouncementCarCreateViewSet
from django.urls import path, include


router = SimpleRouter()

router.register(r"announcementcar/", AnnouncementCarCreateViewSet)

urlpatterns = [
    path("v1/", include(router.urls))
]