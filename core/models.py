from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Place(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(decimal_places=10, max_digits=16, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=16, null=True, blank=True)
    altitude = models.DecimalField(decimal_places=10, max_digits=16, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Publication(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    place = models.ForeignKey(Place, null=True)
    latitude = models.DecimalField(decimal_places=10, max_digits=16, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=16, null=True, blank=True)
    altitude = models.DecimalField(decimal_places=10, max_digits=16, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    begin_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Image(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='core/')
    preview = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    publication = models.ForeignKey(Publication)
    upload_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return str(self.name)
