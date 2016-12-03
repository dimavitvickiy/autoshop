from django.db import models

# Create your models here.
from cars.models import Car
from equipments.models import AdditionEquipment
from persons.models import Manager, Buyer


class Contract(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    addition_equipment = models.ManyToManyField(AdditionEquipment)
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