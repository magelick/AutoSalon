from django.urls import path
from .views import ShopListView, AboutUsTemplateView, NotFoundTemplateView

handler404 = NotFoundTemplateView.as_view()

urlpatterns = [
    path('about/', AboutUsTemplateView.as_view(), name='about'),
    path('', ShopListView.as_view(), name='homepage'),
]