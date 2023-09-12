from django.urls import path
from .views import BrandsListView, ModelsListView,BodyListView, DescriptionListView, CarSearchListView, NotFoundTemplateView


urlpatterns = [
    path('', BrandsListView.as_view(), name='brand_car'),
    path('search/', CarSearchListView.as_view(), name='search'),
    path('<slug:slug>/', ModelsListView.as_view(), name='model_car'),
    path('model/<slug:slug>/', BodyListView.as_view(), name='body_car'),
    path('model/body/<slug:slug>/', DescriptionListView.as_view(), name='descr_car')
]

handler404 = NotFoundTemplateView.as_view()
