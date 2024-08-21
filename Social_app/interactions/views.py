from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer
from .models import Like

class LikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        # Initialize the serializer with the request data
        serializer = self.get_serializer(data=request.data)
        
        # Validate the serializer
        serializer.is_valid(raise_exception=True)
        
        # Save the like
        serializer.save()
        
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
    

    
