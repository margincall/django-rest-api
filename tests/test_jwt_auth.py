from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse

from rest_framework import status

from apps.authentication.models import User


class JSONWebTokenAuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user_a@a.com', password='password_a')
        self.url_obtain_token = reverse('obtain_jwt_token')

    def test_JWT_토큰_생성_후_인증(self):
        response = self.client.get("/", {})
        self.assertNotEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

        response = self.client.post(self.url_obtain_token,
                                    {"email": 'user_a@a.com', "password": 'password_a'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response)

        token = response.data['token']

        response = self.client.get("/", {}, HTTP_AUTHORIZATION='JWT {}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

    def test_JWT_잘못된_유저_정보_토큰_생성_실패(self):
        response = self.client.post(self.url_obtain_token,
                                    {"username": 'user_a', "password": 'wrong_password'},
                                    format='json')

        self.assertNotEqual(response.status_code, status.HTTP_200_OK, msg=response)
