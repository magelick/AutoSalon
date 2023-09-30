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
        brands = AnnouncementCar.objects.all()
        form.fields['brand'].choices = ((brand.car_brand.slug, brand.car_brand.brand) for brand in brands)
        if self.request.GET.get('brand'):
            models = AnnouncementCar.objects.filter(car_model__slug=self.request.GET.get('model'))
            form.fields['model'].choices = ((model.slug, model.model) for model in models)
        if self.request.GET.get('model'):
            bodies = AnnouncementCar.objects.filter(car_body__slug=self.request.GET.get('body'))
            form.fields['body'].choices = ((body.slug, body.body) for body in bodies)
        context['form'] = form
        return context


class CarDetailListView(ListView):
    model = AnnouncementCar
    template_name = 'transport/car.html'
    context_object_name = 'car_details'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = AnnouncementCar.objects.filter(announcement_car_slug=slug)
        return queryset


class NotFoundTemplateView(TemplateView):
    template_name = 'transport/404.html'
