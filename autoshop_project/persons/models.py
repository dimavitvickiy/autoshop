from django.db import models
from django.contrib.auth.models import User

from autoshops.models import Autoshop


class Manager(models.Model):
    account = models.OneToOneField(User, default=0)
    autoshop = models.ForeignKey(Autoshop, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    birthdate = models.DateField()
    passport = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Managers'

    def __str__(self):
        return self.account.first_name


class Buyer(models.Model):
    birthdate = models.DateField()
    passport = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
