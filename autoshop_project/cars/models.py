from django.db import models

# Create your models here.
from factories.models import Factory
from autoshops.models import Autoshop
from car_models.models import Model


class CarState(models.Model):
    car_state = models.CharField(max_length=120, unique=True)


class CarColor(models.Model):
    car_color = models.CharField(max_length=120, unique=True)


class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    no_engine = models.CharField(max_length=20, unique=True)
    no_cab = models.CharField(max_length=20, unique=True)
    autoshop = models.ForeignKey(Autoshop, on_delete=models.CASCADE)
    state = models.ForeignKey(CarState, on_delete=models.CASCADE)
    color = models.ForeignKey(CarColor, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    release_field = models.DateField()
