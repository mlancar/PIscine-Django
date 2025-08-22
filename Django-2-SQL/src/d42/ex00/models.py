from django.db import models

# Create your models here.

class movies(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titre