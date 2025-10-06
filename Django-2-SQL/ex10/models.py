from django.db import models
from django.utils import timezone


# Create your models here.

class Planets(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True, default="Unknown")
    climate = models.CharField(default="Unknown", null=True)
    diameter = models.IntegerField(default=0, null=True)
    orbital_period = models.IntegerField(default=0, null=True)
    population = models.BigIntegerField(default=0, null=True)
    rotation_period = models.IntegerField(default=0, null=True)
    surface_water = models.FloatField(default=0, null=True)
    terrain = models.CharField(default="Unknown", null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.name

class People(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True, default="Unknown")
    birth_year = models.CharField(max_length=32, default="Unknown", null=True)
    gender = models.CharField(max_length=32, default="Unknown")
    eye_color = models.CharField(max_length=32, default="Unknown", null=True)
    hair_color = models.CharField(max_length=32, default="Unknown", null=True)
    height = models.IntegerField(default=0, null=True)
    mass = models.FloatField(default=0, null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, related_name='resident', null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.name

class Movies(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True, default="Unknown")
    episode_nb = models.IntegerField(primary_key=True, default=0)
    opening_crawl = models.TextField(null=True, blank=True, default="Unknown")
    director = models.CharField(null=False, max_length=32, default="Unknown")
    producer = models.CharField(null=False, max_length=128, default="Unknown")
    release_date = models.DateField(null=False, default="27-08-2025")
    characters = models.ManyToManyField(People, related_name='resident', blank=True)

def __str__(self):
    return self.title
