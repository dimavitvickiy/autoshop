from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=120, unique=True)

class Factory(models.Model):
    city = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Factories'