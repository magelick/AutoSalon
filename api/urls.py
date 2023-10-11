from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include


router = SimpleRouter()

router.register(r"1/", views.AnnouncementCarCreateViewSet, basename="announcementcar-create")
router.register(r"2/", views.AnnouncementCarReadViewSet, basename="announcementcar-read")
router.register(r"3/", views.AnnouncementCarUpdateViewSet, basename="announcementcar-update")
router.register(r"4/", views.AnnouncementCarDeleteViewSet, basename="announcementcar-delete")

urlpatterns = [
    path("v1/", include(router.urls))
]