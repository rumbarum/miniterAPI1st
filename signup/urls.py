from django.urls import path
from .views import Signupview


urlpatterns = [
    path('', Signupview.as_view()),
]
