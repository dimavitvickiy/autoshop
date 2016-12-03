from django.shortcuts import render

from .models import Autoshop


def autoshop_list(request):
    autoshops = Autoshop.objects.all()
    context_dict = {
        'autoshops': autoshops,
        'title': 'Home'
    }
    return render(request, 'autoshop_list.html', context=context_dict)


def autoshop_detail(request, slug=None):
    autoshop = Autoshop.objects.get(slug=slug)
    context_dict = {
        'autoshop': autoshop,
        'title': autoshop.name
    }
    return render(request, 'autoshop_detail.html', context=context_dict)