from rest_framework import serializers
from .models import Like, Comment

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [  'post_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [ 'post_id', 'content']

class GetcommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'content', 'user_id']