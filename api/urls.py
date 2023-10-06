from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include


router = SimpleRouter()

router.register(r"create", views.AnnouncementCarCreateViewSet)
router.register(r"read", views.AnnouncementCarReadViewSet)
router.register(r"update", views.AnnouncementCarUpdateViewSet)
router.register(r"delete", views.AnnouncementCarDeleteViewSet)

urlpatterns = [
    path("v1/", include(router.urls))
]