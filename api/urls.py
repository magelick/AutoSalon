from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include


router = SimpleRouter()

router.register(r"create/", views.AnnouncementCarCreateViewSet, basename="announcementcar-create")
router.register(r"read/", views.AnnouncementCarReadViewSet, basename="announcementcar-read")
router.register(r"update/", views.AnnouncementCarUpdateViewSet, basename="announcementcar-update")
router.register(r"delete/", views.AnnouncementCarDeleteViewSet, basename="announcementcar-delete")

urlpatterns = [
    path("v1/", include(router.urls))
]