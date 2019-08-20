from django.urls import path
from tweet.views import Tweetview

urlpatterns = [
    path('', Tweetview.as_view()),
]
