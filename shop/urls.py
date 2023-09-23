from django.urls import path
from .views import ShopListView, AboutUsTemplateView, NotFoundTemplateView, ContactTemplateView

handler404 = NotFoundTemplateView.as_view()

urlpatterns = [
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('about/', AboutUsTemplateView.as_view(), name='about'),
    path('', ShopListView.as_view(), name='homepage'),
]