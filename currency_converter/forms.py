from django import forms

from .request import take_symbs


class CurrencyForm(forms.Form):

    symbols = take_symbs()

    value = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control",
                "required": "true",
            },
        )
    )
    fromCur = forms.CharField(
        required=True,
        widget=forms.Select(
            choices=symbols,
            attrs={
                "class": "form-select",
                "required": "true",
            },
        ),
    )
    toCur = forms.CharField(
        required=True,
        widget=forms.Select(
            choices=symbols,
            attrs={
                "class": "form-select",
                "required": "true",
            },
        ),
    )
