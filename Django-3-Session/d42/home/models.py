from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import Permission


# Create your models here.

class User(AbstractUser):
    reputation = models.IntegerField(default=0)

    def upvote_increase_reputation(self):
        self.reputation += 5
        self.save()
        self.handle_perm()
    
    def upvote_decrease_reputation(self):
        self.reputation -= 5
        self.save()
        self.handle_perm()

    def downvote_decrease_reputation(self):
        self.reputation -= 2
        self.save()
        self.handle_perm()
    
    def downvote_increase_reputation(self):
        self.reputation += 2
        self.save()
        self.handle_perm()

    def balance_reputation(self, tip):
        for user in tip.up_vote.all():
            tip.author.reputation -= 5
            tip.author.handle_perm()
            tip.author.save()
        
        for user in tip.down_vote.all():
            tip.author.reputation += 2
            tip.author.handle_perm()
            tip.author.save()


    def handle_perm(self):
        if self.reputation == 15:
            perm = Permission.objects.get(codename="downvoter")
            self.user_permissions.add(perm)
        
        if self.reputation == 30:
            perm = Permission.objects.get(codename="deleter")
            self.user_permissions.add(perm)
        
        if self.reputation < 15:
            perm = Permission.objects.get(codename="downvoter")
            self.user_permissions.remove(perm)
        
        if self.reputation < 30:
            perm = Permission.objects.get(codename="deleter")
            self.user_permissions.remove(perm)
        self.save()
    
class Tip(models.Model):
    content = models.TextField(max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tips"
    )
    date = models.DateTimeField(auto_now_add=True)
    down_vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvoted_tips', blank=True)
    up_vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvoted_tips', blank=True)
    
    class Meta:
        permissions = [
            ("downvoter", "Can downvote tips"),
            ("deleter", "Can delete tips"),
        ]
    