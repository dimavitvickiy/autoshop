from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse

from engines.models import Engine


class Cab(models.Model):
    cab_type = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.cab_type


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)


class CarModel(models.Model):
    brand = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    volume_fuel = models.FloatField()
    consumption_fuel = models.FloatField()
    engine = models.ForeignKey(Engine, null=True, blank=True, on_delete=models.SET_NULL)
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    number_of_places = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    max_weight = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("car_models:detail", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("car_models:delete", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("car_models:update", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = CarModel.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_saved_model_receive(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_saved_model_receive, sender=CarModel)

