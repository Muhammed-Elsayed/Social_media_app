from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model 
from rest_framework.views import APIView
from .models import Follow

CustomUser = get_user_model()

class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        follower = request.data.get('username')
        if not follower :
            return Response({"error": "your username is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        followed_username = request.data.get('followed_user')
        if not followed_username :
            return Response({"error": "his username is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if follower == followed_username:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follower_object = CustomUser.objects.get(username=follower)
        followed_object = CustomUser.objects.get(username=followed_username)
        follow, created = Follow.objects.get_or_create(follower=follower_object, following=followed_object)

        if created:
            return Response({"message": f"You are now following {followed_object.username}"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You are already following this user."}, status=status.HTTP_200_OK)


class UnfollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        follower = request.data.get('username')
        if not follower:
            return Response({"error": "Your username is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        followed_username = request.data.get('followed_user')
        if not followed_username:
            return Response({"error": "The username of the user to unfollow is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if follower == followed_username:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            follower_object = CustomUser.objects.get(username=follower)
            followed_object = CustomUser.objects.get(username=followed_username)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            follow = Follow.objects.get(follower=follower_object, following=followed_object)
            follow.delete()
            return Response({"message": f"You have unfollowed {followed_object.username}"}, status=status.HTTP_200_OK)
        except Follow.DoesNotExist:
            return Response({"message": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)



