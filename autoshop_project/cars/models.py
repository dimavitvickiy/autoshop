from django.db import models
from django.urls import reverse


# Create your models here.
from factories.models import Factory
from autoshops.models import Autoshop
from car_models.models import CarModel


class CarState(models.Model):
    car_state = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.car_state


class CarColor(models.Model):
    car_color = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.car_color


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    factory = models.ForeignKey(Factory, null=True, blank=True, on_delete=models.SET_NULL)
    no_engine = models.CharField(max_length=20, unique=True)
    no_cab = models.CharField(max_length=20, unique=True)
    autoshop = models.ForeignKey(Autoshop, on_delete=models.CASCADE)
    state = models.ForeignKey(CarState, on_delete=models.PROTECT)
    color = models.ForeignKey(CarColor, on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    release_field = models.DateField()

    def __str__(self):
        return self.model.brand + " | " + self.model.name

    def get_absolute_url(self):
        return reverse("cars:detail", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("cars:delete", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("cars:update", kwargs={"id": self.id})
