from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import CarModel
from .forms import CarModelForm


@login_required
def car_model_create(request):
    form = CarModelForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully created')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, 'Not created')
    context = {
        "button_name": 'Create model',
        "form": form,
        "title": "Create new model"
    }
    return render(request, "car_model_form.html", context)


def car_model_list(request):
    models = CarModel.objects.all()
    context = {
        'models': models,
        'title': 'Models'
    }
    return render(request, 'car_model_list.html', context)


def car_model_detail(request, slug):
    model = get_object_or_404(CarModel, slug=slug)
    context = {
        'model': model,
        "title": model.brand + " | " + model.name,
    }
    return render(request, 'car_model_detail.html', context)


@login_required
def car_model_update(request, slug=None):
    instance = get_object_or_404(CarModel, slug=slug)
    form = CarModelForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "button_name": "Edit model",
        "title": "Edit model",
        "instance": instance,
        "form": form
    }
    return render(request, 'car_model_form.html', context)


@login_required
def car_model_delete(request, slug=None):
    instance = get_object_or_404(CarModel, slug=slug)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully deleted")
        return HttpResponseRedirect("/")
    context = {
        "instance": instance,
        "title": "Delete model",
    }
    return render(request, "confirm_delete.html", context)
