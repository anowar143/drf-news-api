from rest_framework.generics import ListCreateAPIView
from rest_framework import status, permissions
from rest_framework.response import Response

from user.serializers import UserSerializer
from user.models import User


class UserListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.filter()

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(
                first_name=self.request.data['first_name'],
                last_name=self.request.data['last_name'],
                gender=self.request.data.get('gender', 'male'),
                email=self.request.data['email'],
                password=self.request.data['password'],
            )
            serializer = self.get_serializer(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(data={'message': 'cannot create user'}, status=status.HTTP_409_CONFLICT)
