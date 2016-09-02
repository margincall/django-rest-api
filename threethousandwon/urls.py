"""django_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token


from apps.authentication.views import UserViewSet, RestFacebookLogin, facebookTemplate
from apps.artist.views import ArtistViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'artists', ArtistViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token, name='obtain_jwt_token'),
    url(r'^accounts/', include('allauth.urls') ),
    url(r'^facebook/', csrf_exempt(facebookTemplate)),
    #url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(
        r'^rest/facebook-login/$',
        csrf_exempt(RestFacebookLogin.as_view()),
        name='rest_facebook_login'
    ),

]
