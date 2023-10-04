from django.views.generic import TemplateView


class ShopListView(TemplateView):
    template_name = 'shop/index.html'
    context_object_name = 'shop'


class AboutUsTemplateView(TemplateView):
    template_name = 'shop/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'shop/contact.html'

