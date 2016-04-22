from django.shortcuts import render
from Twitter.models import Tweet
from Twitter.serializers import TweetSerializer
from rest_framework import generics

class TweetList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
