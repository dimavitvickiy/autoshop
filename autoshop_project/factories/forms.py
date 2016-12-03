from django import forms

from .models import Factory


class FactoryForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = [
            "name",
            "city",
            "phone",
            "email",
            "country"
        ]
