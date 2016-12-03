from django import forms


from .models import Engine


class EngineForm(forms.ModelForm):
    class Meta:
        model = Engine
        fields = [
            "name",
            "power",
            "image",
            "volume",
            "number_of_cylinders"
        ]
