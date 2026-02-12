from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tip(models.Model):
    content = models.TextField(max_length=500)
    author = models.CharField(max_length=12)
    date = models.DateField(auto_now_add=True)
    down_vote = models.ManyToManyField(User, related_name='downvoted_tips', blank=True)
    up_vote = models.ManyToManyField(User, related_name='upvoted_tips', blank=True)
    