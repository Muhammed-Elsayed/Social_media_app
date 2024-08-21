import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None  # No token, no authentication

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired.')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token yasta.')

        user = CustomUser.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found.')

        return (user, token)  # Return user and token as a tuple

    def authenticate_header(self, request):
        return 'Bearer'
