from django.db import models
from django.conf import settings
from django.utils.timesince import timesince

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="article",
        null=False
    )
    created = models.DateTimeField(auto_now_add=True, null=False)
    synopsis = models.CharField(max_length=312, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

    def time_since_creation(self):
        return timesince(self.created)

class UserFavouriteArticle(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favourited_by_user",
        null=False
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="favourite_article",
        null=False
    )

    def __str__(self):
        return self.article.title
    
    # down_vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvoted_tips', blank=True)
    # up_vote = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvoted_tips', blank=True)