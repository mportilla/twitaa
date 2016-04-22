from rest_framework import serializers
from Twitter.models import Tweet,TweetUser

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('author', 'text', 'created_date')


class TweetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetUser
        fields = ('author.name', 'seguidores')