from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class Factory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("factories:detail", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("factories:delete", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("factories:update", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Factories'


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Factory.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_saved_factory_receive(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_saved_factory_receive, sender=Factory)