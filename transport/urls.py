from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import CarSearchListView, CarDetailListView, NotFoundTemplateView


urlpatterns = [
    path('', CarSearchListView.as_view(), name='search'),
    path('car_details/<slug:slug>/', CarDetailListView.as_view(), name='car_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = NotFoundTemplateView.as_view()
