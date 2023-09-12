from django import forms


class SearchCarsForm(forms.Form):
    brand = forms.CharField(
        required=False
    )
    model = forms.CharField(
        required=False
    )