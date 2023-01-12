from rest_framework import serializers
from users.models import CustomUser

#access토큰 작동 확인용 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"