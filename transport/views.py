from django.views.generic import ListView
from .models import AnnouncementCar, ModelCar, BodyCar
from .forms import SelectCarsForm, SearchCarForm


class CarSearchListView(ListView):
    """
    Класс предствления для странички калатога автомобилей
    """
    model = AnnouncementCar  # Модель
    paginate_by = 9  # Пагинация
    template_name = 'transport/search.html'  # Шаблон
    context_object_name = 'search_car'  # Данные на шаблоне
    queryset = AnnouncementCar.objects.all().order_by('car_brand')  # Query-параметры

    # Метод, отвечающий зя отображения всех объявлений
    def get_queryset(self):
        queryset = self.queryset

        if self.request.GET.get('brand'):  # Если в фильтре выбран Бренд
            queryset = self.queryset.filter(car_brand__slug=self.request.GET.get('brand'))
        elif self.request.GET.get('model'):  # Если в фильтре выбран Модель
            queryset = self.queryset.filter(car_model__slug=self.request.GET.get('model'))
        elif self.request.GET.get('body'):  # Если в в фильтре выбран Кузов модели
            queryset = self.queryset.filter(car_body__slug=self.request.GET.get('body'))

        if self.request.GET.get('car'):  # Если что-то написано в фильтре
            queryset = self.queryset.filter(slug__contains=self.request.GET.get('car'))

        return queryset

    # Метод, отвечающий за фильтр
    def _select_cars_form(self):
        form = SelectCarsForm(self.request.GET)  # Форма фильтра
        brands = AnnouncementCar.objects.all()
        # Расширяем поле Бренда
        form.fields['brand'].choices = [("", "Бренд"), ] + [(brand.car_brand.slug, brand.car_brand.brand_name) for brand
                                                            in set(brands)]
        form.fields['model'].choices = [("", "Модель"), ]

        form.fields['body'].choices = [("", "Кузов"), ]

        form.fields['year_of_issue'].choices = [("", "Год выпуска"), ] + [("", objs) for objs in set(
            obj.car_year_of_issue_type for obj in self.queryset)]

        form.fields['mileage'].choices = [("", "Пробег"), ] + [("", objs) for objs in
                                                               set(obj.car_mileage_type for obj in self.queryset)]

        form.fields['engine_volume'].choices = [("", "Объём двигателя"), ] + [("", objs) for objs in set(
            obj.engine_volume for obj in self.queryset)]

        form.fields['engine_type'].choices = [("", "Тип двигателя"), ] + [("", objs) for objs in set(
            obj.car_engine_type for obj in self.queryset)]

        form.fields['transmission_type'].choices = [("", "Коробка передач"), ] + [("", objs) for objs in set(
            obj.car_transmission_type for obj in self.queryset)]

        form.fields['color'].choices = [("", "Цвет кузова"), ] + [("", objs) for objs in
                                                                  set(obj.car_color_type for obj in self.queryset)]

        form.fields['body_type'].choices = [("", "Тип кузова"), ] + [("", objs) for objs in
                                                                     set(obj.car_body_type for obj in self.queryset)]

        if self.request.GET.get('brand'):  # Если выбран Бренд
            # Расширяем поле Модели кокнретного Бренда
            models = set(ModelCar.objects.filter(announcementcar__car_model__brand__slug=self.request.GET.get('brand')))
            form.fields['model'].choices += [(model.slug, model.model_name) for model in models]

        if self.request.GET.get('model'):  # Если выбрана Модель
            # Расширяем поле кузова
            bodies = set(BodyCar.objects.filter(announcementcar__car_body__model__slug=self.request.GET.get('model')))
            form.fields['body'].choices += [(body.slug, body.body_name) for body in bodies]

        return form

    # Метод, отвечающий за отображение фильтров на шаблоне
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self._select_cars_form()  # Отображаем выборочный фильтр
        context['form2'] = SearchCarForm(self.request.GET)  # Отображаем строчный фильтр
        return context


class CarDetailView(ListView):
    """
    Класс представления, отображаемый даные конкретного объявления
    """
    model = AnnouncementCar  # Модель
    template_name = 'transport/car.html'  # Шаблон
    context_object_name = 'car_details'  # Данные на шаблоне
    queryset = AnnouncementCar.objects.all()  # Query-set параметры

    def get_queryset(self):
        """
        Метод, фильтрующий данные конкретного объявления по слагу
        """
        # Возвращаем данные, отфильтрованные по слагу
        return self.queryset.filter(slug=self.kwargs.get("slug"))

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Метод, отображающий данные конкретного объвления
        """
        context = super().get_context_data(**kwargs)
        car_object = self.get_queryset().first()  # Выводим на шаблон первое совпадающие объявление
        context['equipment_data'] = car_object.equipment.all()  # Вывожим отдельно комплектацию конкретного объявления
        return context
