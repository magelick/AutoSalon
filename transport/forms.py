from django import forms


class SelectCarsForm(forms.Form):
    """
    Форма фильтравого поиска
    """
    # Бренд
    brand = forms.ChoiceField(
        required=False
    )
    # Модель
    model = forms.ChoiceField(
        required=False
    )
    # Кузов
    body = forms.ChoiceField(
        required=False
    )
    # Год выпуска
    year_of_issue = forms.ChoiceField(
        required=False
    )
    # Пробег
    mileage = forms.ChoiceField(
        required=False
    )
    # Тип двигателя
    engine_type = forms.ChoiceField(
        required=False
    )
    # Объём двигателя
    engine_volume = forms.ChoiceField(
        required=False
    )
    # Тип коробки передач
    transmission_type = forms.ChoiceField(
        required=False
    )
    # Цвет кузова
    color = forms.ChoiceField(
        required=False
    )
    # Тип кузова
    body_type = forms.ChoiceField(
        required=False
    )
    # Минимальная цена
    min_price = forms.IntegerField(
        required=False
    )
    # Максимальная цена
    max_price = forms.IntegerField(
        required=False
    )


class SearchCarForm(forms.Form):
    """
    Форма строчнокго поиска автомобиля
    """
    # Конкретный автомобиль
    car = forms.CharField(
        required=False
    )
