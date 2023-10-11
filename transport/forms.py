from django import forms
from .models import AnnouncementCar


class SelectCarsForm(forms.Form):
    brand = forms.ChoiceField(
        required=False
    )
    model = forms.ChoiceField(
        required=False
    )
    body = forms.ChoiceField(
        required=False
    )
    year_of_issue = forms.ChoiceField(
        required=False
    )
    mileage = forms.ChoiceField(
        required=False
    )
    engine_type = forms.ChoiceField(
        required=False
    )
    engine_volume = forms.ChoiceField(
        required=False
    )
    transmission_type = forms.ChoiceField(
        required=False
    )
    color = forms.ChoiceField(
        required=False
    )
    body_type = forms.ChoiceField(
        required=False
    )
    min_price = forms.IntegerField(
        required=False
    )
    max_price = forms.IntegerField(
        required=False
    )


class SearchCarForm(forms.Form):
    car = forms.CharField(
        required=False
    )
