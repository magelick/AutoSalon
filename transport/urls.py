from django.urls import path
from .views import CarSearchListView, CarDetailView

# Список путей к страничкам
urlpatterns = [
    path('', CarSearchListView.as_view(), name='search'),  # Сслыка на страницу каталога автомобилей
    path('car_details/<slug:slug>/', CarDetailView.as_view(), name='car_details')  # Ссылка на страницу
    # кокнетного объявления
]
