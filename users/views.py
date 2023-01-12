from rest_framework import viewsets
from users.serializers import UserSerializer
from users.models import CustomUser

#access토큰이 잘 작동하는지 확인하기 위해 만든 유저정보를 볼 수 있는 API view
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
