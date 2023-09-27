from django.views.generic import ListView, TemplateView
from .models import AnnouncementCar
from .forms import SearchCarsForm


class CarSearchListView(ListView):
    model = AnnouncementCar
    template_name = 'transport/search.html'
    context_object_name = 'search_car'

    def get_queryset(self):
        queryset = AnnouncementCar.objects.all()

        car_brand = self.request.GET.get('brand')
        car_model = self.request.GET.get('model')
        car_body = self.request.GET.get('body')

        if car_brand:
            queryset = queryset.filter(car_brand__slug__contains=car_brand)
        if car_model:
            queryset = queryset.filter(car_model__slug=car_model)
        if car_body:
            queryset = queryset.filter(car_body__slug__contains=car_body)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchCarsForm(self.request.GET)
        # brands = AnnouncementCar.objects.get('car_brand')
        # form.fields['brand'].choices = [(brand.car_brand.slug, brand.car_brand) for brand in brands]
        if self.request.GET.get('brand'):
            models = AnnouncementCar.objects.filter(car_brand__slug=self.request.GET.get('brand'))
            form.fields['model'].choices = [(model.slug, model.car_model) for model in models]
        context['form'] = form
        return context


class NotFoundTemplateView(TemplateView):
    template_name = 'transport/404.html'
