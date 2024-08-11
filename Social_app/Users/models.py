from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='media/photos', blank=True, null=True)
