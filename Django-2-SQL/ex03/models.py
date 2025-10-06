from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True, default="Unknown")
    episode_nb = models.IntegerField(primary_key=True, default=0)
    opening_crawl = models.TextField(null=True, blank=True, default="Unknown")
    director = models.CharField(null=False, max_length=32, default="Unknown")
    producer = models.CharField(null=False, max_length=128, default="Unknown")
    release_date = models.DateField(null=False, default="27-08-2025")

def __str__(self):
    return self.title
