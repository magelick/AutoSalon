from django.http import HttpResponseNotFound

from django.views.generic import TemplateView


class ShopListView(TemplateView):
    template_name = 'shop/homepage.html'
    context_object_name = 'shop'


class AboutUsTemplateView(TemplateView):
    template_name = 'shop/about.html'


class NotFoundTemplateView(TemplateView):
    template_name = 'shop/404.html'
