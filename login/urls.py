from django.urls import path
from login.views import Loginview


urlpatterns = [
    path('',  Loginview.as_view()),
]
