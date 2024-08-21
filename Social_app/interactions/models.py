from django.db import models
from django.contrib.auth import get_user_model
from Post.models import Post 
CustomUser = get_user_model()



class Like(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)