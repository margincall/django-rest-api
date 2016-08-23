from allauth.account.views import LoginView
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialApp, SocialToken, SocialLogin

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter, fb_complete_login
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.decorators import api_view

import sys, traceback


from apps.authentication.serializers import UserSerializer, EverybodyCanAuthentication


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



def facebookTemplate(request):
    return render(request, "facebook.html",{})



class RestFacebookLogin(APIView):
    """
    Login or register a user based on an authentication token coming
    from Facebook.
    Returns user data including session id.
    """

    # this is a public api!!!
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
    authentication_classes = (EverybodyCanAuthentication,)

    #@api_view(['GET', ])
    def dispatch(self, *args, **kwargs):
        pass
        #return Response(status=402, data={
        #    'detail': 'dispatch',
        #})
        return super(RestFacebookLogin, self).dispatch(*args, **kwargs)

    #@api_view(['GET', ])
    def get(self, request, *args, **kwargs):
        request.encoding = "utf-8"

        try:
            #return HttpResponse("123")
            original_request = request._request
            auth_token = request.GET.get('auth_token', '')

            # Find the token matching the passed Auth token
            app = SocialApp.objects.get(provider='facebook')
            fb_auth_token = SocialToken(app=app, token=auth_token)

            # check token against facebook
            login = fb_complete_login(original_request, app, fb_auth_token)
            login.token = fb_auth_token
            login.state = SocialLogin.state_from_request(original_request)

            # add or update the user into users table
            complete_social_login(original_request, login)
            # Create or fetch the session id for this user
            token, _ = Token.objects.get_or_create(user=original_request.user)
            # if we get here we've succeeded
            data = {
                'username': original_request.user.username,
                'objectId': original_request.user.pk,
                'firstName': original_request.user.first_name,
                'lastName': original_request.user.last_name,
                'sessionToken': token.key,
                'email': original_request.user.email,
            }

            print(data)

            return Response(
                status=200,
                data=data
            )

        except:
            traceback.print_exc(file=sys.stdout)
            return Response(status=401, data={
                'detail': 'Bad Access Token',
            })
