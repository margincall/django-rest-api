from django.contrib.auth.models import User

from rest_framework import serializers

from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
                           get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.helpers import complete_social_login


# Serializers define the API representation.
from rest_framework.authentication import TokenAuthentication


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class EverybodyCanAuthentication(TokenAuthentication):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

    def authenticate(self, request):
        return None
