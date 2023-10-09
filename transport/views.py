from django.views.generic import ListView, TemplateView, DetailView
from django.db.models.functions import Lower
from .models import AnnouncementCar
from .forms import SearchCarsForm


class CarSearchListView(ListView):
    model = AnnouncementCar
    paginate_by = 10
    template_name = 'transport/search.html'
    context_object_name = 'search_car'
    queryset = AnnouncementCar.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        car_brand = self.request.GET.get('brand')
        car_model = self.request.GET.get('model')
        car_body = self.request.GET.get('body')

        if car_brand:
            queryset = queryset.filter(car_brand__slug__contains=Lower(car_brand))
        if car_model:
            queryset = self.queryset.filter(car_model__slug=Lower(car_model))
        if car_body:
            queryset = self.queryset.filter(car_body__slug__contains=Lower(car_body))

        return queryset

    def _search_cars_form(self):
        form = SearchCarsForm(self.request.GET)
        brands = AnnouncementCar.objects.all()
        form.fields['brand'].choices = ((brand.car_brand.slug, brand.car_brand.brand_name) for brand in brands)

        if self.request.GET.get('brand'):
            models = AnnouncementCar.objects.filter(car_model__slug=self.request.GET.get('model'))
            form.fields['model'].choices = ((model.slug, model.model_name) for model in models)

        if self.request.GET.get('model'):
            bodies = AnnouncementCar.objects.filter(car_body__slug=self.request.GET.get('body'))
            form.fields['body'].choices = ((body.slug, body.body_name) for body in bodies)

        return form

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self._search_cars_form()
        return context


class CarDetailView(ListView):
    model = AnnouncementCar
    template_name = 'transport/car.html'
    context_object_name = 'car_details'
    queryset = AnnouncementCar.objects.all()

    def get_queryset(self):
        return self.queryset.filter(slug=self.kwargs.get("slug"))


