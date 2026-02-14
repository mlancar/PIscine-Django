from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    reputation = models.IntegerField(default=0)

    def upvote_increase_reputation(self):
        self.reputation += 5
        self.save()
    
    def upvote_decrease_reputation(self):
        self.reputation -= 5
        self.save()

    def downvote_decrease_reputation(self):
        self.reputation -= 2
        self.save()
    
    def downvote_increase_reputation(self):
        self.reputation += 2
        self.save()
    

    def balance_reputation(self, upvote, downvote):
        print("reputation = ", self.reputation)
        print("upvote = ", upvote)
        print("downvote = ", downvote)
        self.reputation -=  (upvote * 5)
        self.reputation += (downvote * 2)
        print("reputation = ", self.reputation)
        self.save()
    



class Tip(models.Model):
    content = models.TextField(max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tips"
    )
    date = models.DateField(auto_now_add=True)
    down_vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvoted_tips', blank=True)
    up_vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvoted_tips', blank=True)
    
    class Meta:
        permissions = [
            ("downvoter", "Can downvote tips"),
        ]
    