from django.shortcuts import render
from Twitter.models import Tweet
from rest_framework import generics
from django.views.generic import ListView
from django.utils import timezone

class TweetList(ListView):
    context_object_name = 'tweets'
    def get_queryset(self):
        queryset = Tweet.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return queryset