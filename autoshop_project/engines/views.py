from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Engine
from .forms import EngineForm


@login_required
def engine_create(request):
    form = EngineForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully created')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, 'Not created')
    context = {
        "button_name": 'Create engine',
        "form": form,
        "title": "Create new engine"
    }
    return render(request, "engine_form.html", context)


def engines_list(request):
    engines = Engine.objects.all()
    context = {
        'engines': engines,
        'title': 'Engines'
    }
    return render(request, 'engine_list.html', context)


def engine_detail(request, slug):
    engine = get_object_or_404(Engine, slug=slug)
    context = {
        'engine': engine,
        "title": engine.name
    }
    return render(request, 'engine_detail.html', context)


@login_required
def engine_delete(request, slug=None):
    instance = get_object_or_404(Engine, slug=slug)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully deleted")
        return HttpResponseRedirect("/")
    context = {
        "instance": instance,
        "title": "Delete engine",
    }
    return render(request, "confirm_delete.html", context)


@login_required
def engine_update(request, slug=None):
    instance = get_object_or_404(Engine, slug=slug)
    form = EngineForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "button_name": "Edit engine",
        "title": "Edit engine",
        "instance": instance,
        "form": form
    }
    return render(request, 'engine_form.html', context)
