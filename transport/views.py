from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, TemplateView
from .models import BrandCar, ModelCar
from django.http import HttpResponseNotFound
from .forms import SearchCarsForm


class BrandsListView(ListView):
    model = BrandCar
    template_name = 'transport/brand.html'
    context_object_name = 'brands'
    ordering = 'brand'


class ModelsListView(ListView):
    model = ModelCar
    template_name = 'transport/model.html'
    context_object_name = 'models'
    ordering = 'model'

    def get_queryset(self):
        brand_slug = self.kwargs.get('slug')
        brand = get_object_or_404(BrandCar, slug=brand_slug)
        return get_list_or_404(ModelCar, brand=brand)


class OneCarListView(ListView):
    model = ModelCar
    template_name = 'transport/one_car.html'
    context_object_name = 'one_car'

    def get_queryset(self):
        model_slug = self.kwargs.get('slug')
        model = get_object_or_404(ModelCar, slug=model_slug)
        return get_list_or_404(ModelCar, model=model)


class CarSearchListView(ListView):
    model = ModelCar
    template_name = 'transport/search_form.html'
    context_object_name = 'search_car'

    def get_queryset(self):
        if 'brand' not in self.request.GET:
            return self.model.objects.all()
        elif 'model' not in self.request.GET:
            return self.model.objects.filter(brand__slug=self.request.GET.get('brand'))
        else:
            return self.model.objects.filter(model__slug=self.request.GET.get('model'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchCarsForm(self.request.GET)
        if self.request.GET.get('brand'):
            models = self.model.objects.filter(brand__slug=self.request.GET.get('brand'))
            form.fields['model'].choices = [(model.model,) for model in models]
        context['form'] = form
        return context


class NotFoundTemplateView(TemplateView):
    template_name = 'transport/404.html'
