from django.urls import path
from .views import CarSearchListView, NotFoundTemplateView


urlpatterns = [
    path('', CarSearchListView.as_view(), name='search'),
]

handler404 = NotFoundTemplateView.as_view()
