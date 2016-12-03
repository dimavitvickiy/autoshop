from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.db.models.query_utils import Q

from .models import Factory
from .forms import FactoryForm


@login_required
def factory_create(request):
    form = FactoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully created')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, 'Not created')
    context = {
        "button_name": 'Create factory',
        "form": form,
        "title": "Create new factory"
    }
    return render(request, "factory_form.html", context)


def factory_list(request):
    factories = Factory.objects.all()
    query = request.GET.get('q')
    if query:
        factories = factories.filter(
            Q(name__icontains=query) |
            Q(city__icontains=query) |
            Q(country__name__icontains=query)
        )
    context = {
        'factories': factories,
        'title': 'Factories'
    }
    return render(request, 'factory_list.html', context)


def factory_detail(request, slug):
    factory = get_object_or_404(Factory, slug=slug)
    context = {
        'factory': factory,
        "title": factory.name,
    }
    return render(request, 'factory_detail.html', context)


@login_required
def factory_update(request, slug=None):
    instance = get_object_or_404(Factory, slug=slug)
    form = FactoryForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "button_name": "Edit factory",
        "title": "Edit factory",
        "instance": instance,
        "form": form
    }
    return render(request, 'factory_form.html', context)


@login_required
def factory_delete(request, slug=None):
    instance = get_object_or_404(Factory, slug=slug)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully deleted")
        return HttpResponseRedirect("/")
    context = {
        "instance": instance,
        "title": "Delete factory",
    }
    return render(request, "confirm_delete.html", context)