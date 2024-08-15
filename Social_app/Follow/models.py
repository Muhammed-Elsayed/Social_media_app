from django.db import models
from django.conf import settings

class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='following',  # This user is following others
        on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='followers',  # This user is being followed by others
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
