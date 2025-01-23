from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer
from rest_framework import serializers

from grades.models import Grade

class Grades_serializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade','id_user','created_at']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password']


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id','username', 'password']