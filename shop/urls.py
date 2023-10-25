from django.urls import path
from .views import ShopListView, AboutUsTemplateView, ContactTemplateView

# Список путей к страничкам
urlpatterns = [
    path('contact/', ContactTemplateView.as_view(), name='contact'),  # Ссылка на страницу Контакты
    path('about/', AboutUsTemplateView.as_view(), name='about'),  # Ссылка на страницу О нас
    path('', ShopListView.as_view(), name='homepage'),  # Ссылка на Домашную страницу
]
