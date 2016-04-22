from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField(max_length=140)
    tweet_resp = models.ForeignKey('Tweet',blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    liked_by = models.ManyToManyField(User,blank=True,related_name='liked_tweer')

    def __str__(self):
        return self.text

    def ls_comment(self):
        return bool(tweet_resp)

class TweetUser(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    seguidores = models.ManyToManyField('TweetUser',blank=True,related_name='followed_by')