from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer, CommentSerializer, GetcommentSerializer
from .models import Like, Comment
from Post.models import Post
from Users.models import CustomUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Like"],
        request_body=LikeSerializer,
        responses={
            201: openapi.Response(description="Post liked successfully"),
            404: openapi.Response(description="Post not found or already liked"),
        },
        operation_description="Like a post by providing the post ID.",
    )

    def post(self, request):
        data = request.data
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
        else:
            return Response({"detail": "post you are trying to like is not found "}, status=status.HTTP_404_NOT_FOUND)

        post = validated_data.get('post_id') #post object
        user = request.user #user object

        try :
            if  Like.objects.get(post_id=post, user_id=user):
                return Response ({"Detial": "The post is already liked"}, status=status.HTTP_404_NOT_FOUND)
            
        except Like.DoesNotExist:
            serializer.save(post_id=post, user_id=user)
            return Response({"Detail":"Post liked successfully"}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        tags=["Like"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the post to unlike'),
            },
            required=['post_id']
        ),
        responses={
            204: openapi.Response(description="Post unliked successfully"),
            404: openapi.Response(description="Post or like not found"),
            400: openapi.Response(description="Invalid data or action"),
        },
        operation_description="Unlike a post by providing the post ID.",
    )

    def delete(self, request):
        post_id = request.data.get('post_id')  
        user = request.user


        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Like instance based on user and post
        try:
            like_instance = Like.objects.get(post_id=post_id, user_id=user)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)

        # If the Like instance is found, delete it
        like_instance.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
    

class CreateComment(APIView):
    permission_classes =[IsAuthenticated]
    @swagger_auto_schema(
        tags=["Comment"],
        request_body=CommentSerializer,
        responses={
            201: openapi.Response(description="Comment created successfully"),
            404: openapi.Response(description="Post not found"),
            400: openapi.Response(description="Invalid data or action"),
        },
        operation_description="Create a comment on a post.",
    )
    def post(self, request):
        user = request.user
        post_id = request.data.get('post_id')
        content = request.data.get('content')
        
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        comment = Comment.objects.create(
            user_id=user,
            post_id=post,
            content=content
        )

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        tags=["Comment"],
        request_body=CommentSerializer,
        responses={
            200: openapi.Response(description="Comment updated successfully"),
            404: openapi.Response(description="Comment or post not found"),
            400: openapi.Response(description="Invalid data or action"),
        },
        operation_description="Update a comment on a post.",
    )
    def put(self, request):
        user = request.user
        comment_id= request.data.get('comment_id')
        post_id=request.data.get('post_id')
        content=request.data.get('content')

        try :
            comment = Comment.objects.get(id=comment_id, post_id=post_id) 
        except Comment.DoesNotExist:
            return Response({"Detail": "Comment doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        comment.content=content
        comment.save()

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=["Comment"],
        
        responses={
            200: openapi.Response(
                description="Comments retrieved successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'content': openapi.Schema(type=openapi.TYPE_STRING),
                            # Add other comment fields here as needed
                        }
                    )
                )
            ),
            404: openapi.Response(description="Post does not exist."),
        },
        operation_description="Retrieve all comments for a specific post.",
    )
    def get(self, request):
        post_id = request.data.get('post_id')

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        all_comments = Comment.objects.filter(post_id=post)
        serializer = GetcommentSerializer(all_comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )
    
    @swagger_auto_schema(
        tags=["Comment"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the post'),
                'comment_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the comment to delete'),
            },
            required=['post_id', 'comment_id']
        ),
        responses={
            204: openapi.Response(description="Comment deleted successfully"),
            404: openapi.Response(description="Comment or post not found"),
            400: openapi.Response(description="Invalid data or action"),
        },
        operation_description="Delete a comment from a post.",
    )
    
    def delete(self, request):
        post_id = request.data.get('post_id')
        comment_id = request.data.get('comment_id')

        if not comment_id or not post_id:
            return Response({"detail": "Both comment_id and post_id are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            comments_to_delete = Comment.objects.filter(id=comment_id, post_id=post_id)

            if not comments_to_delete.exists():
                return Response({"detail": "Comment does not exist or does not belong to the specified post."}, status=status.HTTP_404_NOT_FOUND)
            
            comments_to_delete.delete()
            
            return Response({"detail": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception :
            return Response({"detail": "error happened"}, status=status.HTTP_404_NOT_FOUND)
