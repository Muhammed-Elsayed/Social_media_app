from django.conf import settings
from django.db import models

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower_relatedname', on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_relatedname', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')  # Ensure a unique relationship




