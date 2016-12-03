from django.shortcuts import render, get_object_or_404

from django.db.models.query_utils import Q

from .models import Autoshop
from cars.models import Car
from persons.models import Manager


def autoshop_list(request):
    autoshops = Autoshop.objects.all()
    query = request.GET.get('q')
    if query:
        autoshops = autoshops.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query)
        )
    context_dict = {
        'autoshops': autoshops,
        'title': 'Home'
    }
    return render(request, 'autoshop_list.html', context=context_dict)


def autoshop_detail(request, slug=None):
    autoshop = get_object_or_404(Autoshop, slug=slug)
    cars = Car.objects.filter(autoshop=autoshop)
    can_add_car = False
    if request.user.is_authenticated:
        manager = Manager.objects.filter(account=request.user, autoshop=autoshop).first()
        if manager:
            can_add_car = True
        else:
            cars = cars.filter(state=2)
    else:
        cars = cars.filter(state=2)
    context = {
        'autoshop': autoshop,
        'cars': cars,
        'title': autoshop.name,
        'can_add_car': can_add_car
    }
    return render(request, 'autoshop_detail.html', context=context)