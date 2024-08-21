from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Post(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

