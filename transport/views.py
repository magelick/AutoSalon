from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, TemplateView
from .models import BrandCar, ModelCar, BodyCar, Description
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


class BodyListView(ListView):
    model = BodyCar
    template_name = 'transport/body.html'
    context_object_name = 'body_car'

    def get_queryset(self):
        model_slug = self.kwargs.get('slug')
        model = get_object_or_404(ModelCar, slug=model_slug)
        return get_list_or_404(BodyCar, model=model)


class DescriptionListView(ListView):
    model = Description
    template_name = 'transport/descr.html'
    context_object_name = 'description_car'

    def get_queryset(self):
        body_slug = self.kwargs.get('slug')
        body = get_object_or_404(BodyCar, slug=body_slug)
        return get_list_or_404(Description, body=body)


class CarSearchListView(ListView):
    template_name = 'transport/search_form.html'
    context_object_name = 'search_car'

    def get_queryset(self):
        if 'brand' not in self.request.GET:
            return BrandCar.objects.all()
        elif 'model' not in self.request.GET:
            return BrandCar.brand.models.filter(brand__slug=self.request.GET.get('brand'))
        elif 'body' not in self.request.GET:
            return ModelCar.model.bodies.filter(model__slug=self.request.GET.get('model'))
        else:
            return BodyCar.body.descriptions.all()

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
