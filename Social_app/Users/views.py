from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import CustomUser
import jwt, datetime
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
   permission_classes = [AllowAny]
   def post(self, request):
     serializer = UserSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response(serializer.data)
  
class LoginView(APIView):
    permission_classes = [AllowAny]
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

       response.set_cookie(key='jwt',value=token, httponly=True)
       response.data={
          'jwt':token
       }
       return response




    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response