from django.db import models

# Create your models here.

class Tip(models.Model):
    content = models.TextField(max_length=500)
    author = models.CharField(max_length=12)
    date = models.DateField(auto_now_add=True)

