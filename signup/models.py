from django.db import models


class Signup(models.Model): 
    user_id = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_profile = models.CharField(max_length=50)
    user_csrf = models.CharField(max_length=100)