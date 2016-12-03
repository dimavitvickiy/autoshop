from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)


class Engine(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True)
    power = models.PositiveIntegerField()
    volume = models.FloatField()
    number_of_cylinders = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("engines:detail", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("engines:delete", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("engines:update", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Engine.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_saved_engine_receive(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_saved_engine_receive, sender=Engine)