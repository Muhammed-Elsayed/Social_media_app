from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

CustomUser = get_user_model()


class CreatePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post=serializer.save(user_id=request.user)
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'The post didnot exist'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            post.delete()
        except :
            return Response({'detail': 'wasnot deleted'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"Details": "Post deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    

class PostListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_context(self):
        return {'request': self.request}