from django.urls import path
from .views import CarSearchListView, CarDetailView

urlpatterns = [
    path('', CarSearchListView.as_view(), name='search'),
    path('car_details/<slug:slug>/', CarDetailView.as_view(), name='car_details')
]
