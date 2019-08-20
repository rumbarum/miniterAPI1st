from django.urls import path
from user_auth.views import User_auth

urlpatterns = [
    path('', User_auth.as_view()),
]
