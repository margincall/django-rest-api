from rest_framework import viewsets

from apps.authentication.serializers import UserSerializer
from apps.authentication.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
