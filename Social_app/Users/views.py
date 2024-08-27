from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializers import UserSerializer,canFollowSerializer
from rest_framework.response import Response
from .models import CustomUser
import jwt, datetime
from rest_framework.permissions import AllowAny
from rest_framework import status

USERS_TAG = "Users"
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterView(APIView):
   permission_classes = [AllowAny]

   @swagger_auto_schema(
        tags=[USERS_TAG],
        request_body=UserSerializer,
        responses={201: 'Registered successfully', 400: 'Invalid data'},
    )
   def post(self, request):
     serializer = UserSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response({"detai" : "registered successfully" }, status=status.HTTP_201_CREATED)
  
class LoginView(APIView):
   permission_classes = [AllowAny]

   @swagger_auto_schema(
        tags=[USERS_TAG],
        operation_description="Login a user and receive a JWT token.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            },
            required=['email', 'password']
        ),
        responses={200: openapi.Response(description="JWT token returned"),
                   401: "Unauthorized", 400: "Invalid data"},
    )
   def post(self, request):
       email = request.data['email']
       password = request.data['password']

       user = CustomUser.objects.filter(email=email).first()

       if user is None:
          raise(AuthenticationFailed('User not found'))
       

       if not user.check_password(password):
          raise(AuthenticationFailed('Incorrect password'))
       payload = {
          'id' : user.id,
          'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=60),
          'iat' : datetime.datetime.now(datetime.timezone.utc)
       } 
       token = jwt.encode(payload, 'secret', algorithm='HS256')
       response = Response()

       response.set_cookie(key='jwt',value=token)
       response.data={
          'jwt':token
       }
       return response

class LogoutView(APIView):
    @swagger_auto_schema(
        tags=[USERS_TAG],
        operation_description="Logout a user by deleting the JWT token, No parameters requeired",
        responses={200: "Successfully logged out"}
    )
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success logout'
        }
        return response
    
class AllUsers(APIView):
    @swagger_auto_schema(
        tags=[USERS_TAG],
        operation_description="Retrieve a list of users that the authenticated user can follow.",
        responses={200: canFollowSerializer(many=True)},
    )
    def get(self, request):
        users = CustomUser.objects.exclude(id=request.user.id)
        serializer = canFollowSerializer(users, many=True)
        return Response(serializer.data)