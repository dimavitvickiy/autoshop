from django import forms

from .models import AdditionEquipment


class AdditionEquipmentForm(forms.ModelForm):

    class Meta:
        model = AdditionEquipment
        fields = [
            "name",
            "price"
        ]