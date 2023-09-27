from django import forms


class SearchCarsForm(forms.Form):
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
    # price = forms.CharField(
    #     required=False
    # )