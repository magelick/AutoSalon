from django.views.generic import ListView
from .models import AnnouncementCar, ModelCar, BodyCar, YearOfIssueType
from .forms import SearchCarsForm


class CarSearchListView(ListView):
    model = AnnouncementCar
    paginate_by = 10
    template_name = 'transport/search.html'
    context_object_name = 'search_car'
    queryset = AnnouncementCar.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        if self.request.GET.get('brand'):
            queryset = self.queryset.filter(car_brand__slug=self.request.GET.get('brand'))
        if self.request.GET.get('model'):
            queryset = self.queryset.filter(car_model__slug=self.request.GET.get('model'))
        if self.request.GET.get('body'):
            queryset = self.queryset.filter(car_body__slug=self.request.GET.get('body'))
        if self.request.GET.get('year_of_issue'):
            queryset = self.queryset.filter(year_of_issue=self.request.GET.get('year_of_issue'))

        return queryset

    def _search_cars_form(self):
        form = SearchCarsForm(self.request.GET)
        brands = AnnouncementCar.objects.all()
        form.fields['brand'].choices = [("", "Бренд"), ] + [(brand.car_brand.slug, brand.car_brand.brand_name) for brand
                                                            in brands]
        form.fields['model'].choices = [("", "Модель"), ]
        form.fields['body'].choices = [("", "Кузов"), ]
        form.fields['year_of_issue'].choices = [("", "Год выпуска"), ]
        form.fields['mileage'].choices = [("", "Пробег"), ]
        form.fields['engine_volume'].choices = [("", "Объём двигателя"), ]
        form.fields['engine_type'].choices = [("", "Тип двигателя"), ]
        form.fields['transmission_type'].choices = [("", "Коробка передач"), ]
        form.fields['color'].choices = [("", "Цвет кузова"), ]
        form.fields['body_type'].choices = [("", "Тип кузова"), ]

        if self.request.GET.get('brand'):
            models = ModelCar.objects.filter(announcementcar__car_model__brand__slug=self.request.GET.get('brand'))
            form.fields['model'].choices += [(model.slug, model.model_name) for model in models]

        if self.request.GET.get('model'):
            bodies = BodyCar.objects.filter(announcementcar__car_body__model__slug=self.request.GET.get('model'))
            form.fields['body'].choices += [(body.slug, body.body_name) for body in bodies]

        if self.request.GET.get('body'):
            years = YearOfIssueType.objects.filter(announcementcar__car_year_of_issue_type__slug=self.request.GET.get('body'))
            form.fields['year_of_issue'].choices += [(year.slug, year.year_of_issue) for year in years]

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        car_object = self.get_queryset().first()
        context['equipment_data'] = car_object.equipment.all()
        return context
