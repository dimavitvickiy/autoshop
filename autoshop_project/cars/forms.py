from django import forms

from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            "model",
            "factory",
            "no_engine",
            "no_cab",
            "state",
            "color",
            "price",
            "release_field"
        ]