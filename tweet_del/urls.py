from django.urls import path
from tweet_del.views import Tweet_del

urlpatterns = [
    path('', Tweet_del.as_view()),
]
