from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
      class Meta:
          model = Post
          fields = [ 'image_url', 'content']


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'created_at', 'updated_at']