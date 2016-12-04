from django.db import models
from django.urls import reverse


# Create your models here.
class AdditionEquipment(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("equipments:detail", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("equipments:delete", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("equipments:update", kwargs={"id": self.id})