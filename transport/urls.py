from django.urls import path
from .views import BrandsListView, ModelsListView, OneCarListView, CarSearchListView, NotFoundTemplateView


urlpatterns = [
    path('', BrandsListView.as_view(), name='brand_car'),
    path('search/', CarSearchListView.as_view(), name='search'),
    path('<slug:slug>/', ModelsListView.as_view(), name='model_car'),
    path('model/<slug:slug>/', OneCarListView.as_view(), name='one_car'),
]

handler404 = NotFoundTemplateView.as_view()
