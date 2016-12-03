from django import forms


from .models import CarModel


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = [
            "brand",
            "name",
            "image",
            "volume_fuel",
            "consumption_fuel",
            "engine",
            "cab",
            "number_of_places",
            "price",
            "max_weight"
        ]
