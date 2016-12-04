from django.db import models
from django.urls import reverse

from cars.models import Car
from equipments.models import AdditionEquipment
from persons.models import Manager


class Contract(models.Model):
    manager = models.ForeignKey(Manager, null=True, blank=True, on_delete=models.SET_NULL)
    buyer_birthdate = models.DateField()
    buyer_name = models.CharField(max_length=200)
    buyer_last_name = models.CharField(max_length=200)
    buyer_passport = models.CharField(max_length=20)
    buyer_phone = models.CharField(max_length=20)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    addition_equipment = models.ManyToManyField(AdditionEquipment, blank=True)
    price = models.IntegerField()
    deal_date = models.DateField()
    DEAL_TYPE = (
        ('TD', 'Test-Drive'),
        ('SL', 'Sale')
    )
    deal_type = models.CharField(
        max_length=2,
        choices=DEAL_TYPE,
        default='SL'
    )

    def get_absolute_url(self):
        return reverse("contracts:detail", kwargs={"id": self.id})

