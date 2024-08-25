from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer
from .models import Like
from Post.models import Post

class LikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.user
        post_id = request.data.get('post_id')

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if Like.objects.filter(post_id=post_id, user_id=user_id).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
    

class UnlikeView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        post_id = request.data.get('post_id')  
        user_id = request.user  

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Like instance based on user and post
        try:
            like_instance = Like.objects.get(post_id=post_id, user_id=user_id)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)

        # If the Like instance is found, delete it
        like_instance.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)