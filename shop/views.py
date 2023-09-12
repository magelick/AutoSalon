from django.http import HttpResponseNotFound

from .models import Shop
from django.views.generic import ListView
from django.views.generic import TemplateView


class ShopListView(ListView):
    model = Shop
    template_name = 'shop/homepage.html'
    context_object_name = 'shop'


class AboutUsTemplateView(TemplateView):
    template_name = 'shop/about.html'


# class NotFoundTemplateView(TemplateView):
#     template_name = 'shop/404.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         return HttpResponseNotFound("К сожалению, страница не найдена!")
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['404'] = NotFoundTemplateView.dispatch
#         return context
