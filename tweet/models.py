from django.db import models

class Tweet(models.Model):
    user_id = models.CharField(max_length=50)
    user_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
