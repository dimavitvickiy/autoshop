from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = [
            "buyer_name",
            "buyer_last_name",
            "buyer_birthdate",
            "buyer_passport",
            "buyer_phone",
            "addition_equipment",
            "deal_date",
            "deal_type",
        ]