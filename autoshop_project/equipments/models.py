from django.db import models

# Create your models here.
class AdditionEquipment(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
