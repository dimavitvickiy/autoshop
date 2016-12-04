from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import AdditionEquipmentForm
from .models import AdditionEquipment


@login_required
def equipment_create(request):
    form = AdditionEquipmentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully created')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, 'Not created')
    context = {
        "button_name": 'Add equipment',
        "form": form,
        "title": "Add new equipment"
    }
    return render(request, "equipment_form.html", context)


def equipment_detail(request, id):
    equipment = get_object_or_404(AdditionEquipment, id=id)
    context = {
        'equipment': equipment,
        "title": equipment.name,
    }
    return render(request, 'equipment_detail.html', context)


def equipment_list(request):
    equipments = AdditionEquipment.objects.all()
    query = request.GET.get('q')
    context = {
        'equipments': equipments,
        'title': 'Factories'
    }
    return render(request, 'equipment_list.html', context)


@login_required
def equipment_update(request, id):
    instance = get_object_or_404(AdditionEquipment, id=id)
    form = AdditionEquipmentForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "button_name": "Edit equipment",
        "title": "Edit equipment",
        "instance": instance,
        "form": form,
    }
    return render(request, 'equipment_form.html', context)


@login_required
def equipment_delete(request, id=id):
    instance = get_object_or_404(AdditionEquipment, id=id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully deleted")
        return HttpResponseRedirect("/")
    context = {
        "instance": instance,
        "title": "Delete equipment",
    }
    return render(request, "confirm_delete.html", context)
