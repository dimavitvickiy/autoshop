from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from contracts.forms import ContractForm
from equipments.models import AdditionEquipment
from .forms import CarForm
from .models import Car, CarState
from persons.models import Manager


@login_required
def car_create(request):
    form = CarForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autoshop = Manager.objects.filter(account=request.user).first().autoshop
            instance.save()
            messages.success(request, 'Successfully created')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, 'Not created')
    context = {
        "button_name": 'Add car',
        "form": form,
        "title": "Add new car"
    }
    return render(request, "car_form.html", context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    can_edit = False
    if request.user.is_authenticated:
        manager = Manager.objects.filter(account=request.user, autoshop=car.autoshop).first()
        if manager:
            can_edit = True
    context = {
        'car': car,
        "title": car.model.brand + " | " + car.model.name,
        "can_edit": can_edit
    }
    return render(request, 'car_detail.html', context)


@login_required
def car_update(request, id):
    instance = get_object_or_404(Car, id=id)
    get_object_or_404(Manager, account=request.user, autoshop=instance.autoshop)
    form = CarForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "button_name": "Edit car",
        "title": "Edit car",
        "instance": instance,
        "form": form,
    }
    return render(request, 'car_form.html', context)


@login_required
def car_delete(request, id=id):
    instance = get_object_or_404(Car, id=id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully deleted")
        return HttpResponseRedirect("/")
    context = {
        "instance": instance,
        "title": "Delete car",
    }
    return render(request, "confirm_delete.html", context)


@login_required
def car_sell(request, id):
    form = ContractForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.car = Car.objects.filter(id=id).first()
            instance.manager = Manager.objects.filter(account=request.user).first()
            instance.price = instance.car.price
            instance.save()
            form.save_m2m()
            car = get_object_or_404(Car, id=id)
            if instance.deal_type == 'SL':
                for eqp in instance.addition_equipment.all():
                    instance.price += eqp.price
                instance.save()
                sold_state = CarState.objects.get(id=1)
                car.state = sold_state
                car.save()
                messages.success(request, 'Successfully sold')
            else:
                instance.price = 500
                instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, 'Not created')
    context = {
        "button_name": 'Sell car',
        "form": form,
        "title": "Sell car"
    }
    return render(request, "contract_form.html", context)