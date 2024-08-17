from django.contrib import admin
from .models import Follow  # Import your model

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')  # Customize fields to display

