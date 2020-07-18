import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from django.conf import settings

from user.models import User
from rest_framework.response import Response
from rest_framework import status


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.headers.get('Authorization'):
            pass
        else:
            token = str(request.headers['Authorization']).split(' ', 1)[1]
            data = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithm='HS256')
            try:
                user = User.objects.get(pk=data['id'])
                if not user.is_active:
                    return Response({'message': 'inactive user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                setattr(request, 'user', user)
            except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist) as e:
                return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        response = self.get_response(request)
        return response
