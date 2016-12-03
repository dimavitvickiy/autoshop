from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)


class Autoshop(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    no_bank_card = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("autoshops:detail", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Autoshop.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_saved_autoshop_receive(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_saved_autoshop_receive, sender=Autoshop)