from django.views.generic import ListView, TemplateView
from .models import BrandCar, ModelCar, BodyCar
from .forms import SearchCarsForm


class CarSearchListView(ListView):
    template_name = 'transport/search_form.html'
    context_object_name = 'search_car'

    def get_queryset(self):
        if 'brand' not in self.request.GET:
            return BrandCar.objects.all()
        elif 'model' not in self.request.GET:
            return BrandCar.models.filter(brand__slug=self.request.GET.get('brand'))
        elif 'body' not in self.request.GET:
            return ModelCar.bodies.filter(model__slug=self.request.GET.get('model'))
        else:
            return BodyCar.descriptions.filter(body__slug=self.request.GET.get('model'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchCarsForm(self.request.GET)
        context['form'] = form
        return context


class NotFoundTemplateView(TemplateView):
    template_name = 'transport/404.html'
