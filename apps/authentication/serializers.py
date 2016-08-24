from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication

from apps.authentication.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class GlobalAuthentication(TokenAuthentication):
    def authenticate(self, request):
        return None

