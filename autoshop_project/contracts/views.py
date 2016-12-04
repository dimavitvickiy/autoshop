from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Contract
from persons.models import Manager


@login_required
def contract_list(request):
    manager = Manager.objects.filter(account=request.user).first()
    contracts = Contract.objects.filter(car__autoshop=manager.autoshop).all()
    context = {
        'contracts': contracts,
        'title': 'Contracts'
    }
    return render(request, 'contract_list.html', context)


@login_required
def contract_detail(request, id):
    contract = get_object_or_404(Contract, id=id)
    addition_equipment = contract.addition_equipment.all()
    context = {
        'contract': contract,
        "title": "Contract details",
        'addition_equipment': addition_equipment
    }
    return render(request, 'contract_detail.html', context)
