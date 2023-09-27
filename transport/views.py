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
        context['form'] = form
        return context


class NotFoundTemplateView(TemplateView):
    template_name = 'transport/404.html'
