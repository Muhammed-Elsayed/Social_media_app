from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

CustomUser = get_user_model()


class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        tags=["Posts"],
        request_body=PostSerializer,
        responses={
            201: PostSerializer,
            400: "Invalid data",
            404: "Post not found",
        },
        operation_description="Create a new post and associate it with the authenticated user.",
    )
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post=serializer.save(user_id=request.user)
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        tags=["Posts"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the post to delete'),
            },
            required=['post_id']
        ),
        responses={
            204: "Post deleted successfully",
            404: "Post not found",
        },
        operation_description="Delete a post by its ID.",
    )


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

    @swagger_auto_schema(
        tags=["Posts"],
        responses={
            200: PostSerializer(many=True),
            401: "Unauthorized",
        },
        operation_description="Retrieve a list of all posts.",
    )

    def get_serializer_context(self):
        return {'request': self.request}