from django.conf.urls import include, url
from . import api_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
        url(r'^list/$', api_views.TweetList.as_view()),
 ]