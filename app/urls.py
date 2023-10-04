from rest_framework import routers
from django.urls import path, include
from .views import AnnouncementCarApiView

router = routers.DefaultRouter()

router.register(r'announcements/v1', AnnouncementCarApiView)

urlpatterns = [
    path('', include(router.urls))
]