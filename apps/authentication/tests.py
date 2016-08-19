from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from apps.authentication.models import User


class UserModelTest(TestCase):
    def test_User_생성_및_문자열_표현_확인(self):
        email = 'email@email.com'
        user = User.objects.create_user(email, 'password')
        self.assertEqual(email, str(user))

    def test_Superuser_생성_및_권한_확인(self):
        user = User.objects.create_superuser('admin@email.com', 'password')
        self.assertTrue(user.is_admin)

    def test_Email_없이_User_생성할_때_실패(self):
        self.assertRaises(ValueError, lambda: User.objects.create_user('', 'password'))

    def test_올바르지_않은_Email_User_생성할_때_실패(self):
        self.assertRaises(ValueError, lambda: User.objects.create_user('is#this.email', 'password'))


class UserAPITests(APITestCase):

    def test_API_에서_생성된_User_객체를_받아오는지_확인(self):
        email = 'green@day.com'
        User.objects.create_user(email=email, password='password')

        # JWT Authentication
        response = self.client.post(reverse('obtain_jwt_token'),
                                    {"email": 'green@day.com', "password": 'password'},
                                    format='json')
        token = response.data['token']

        response = self.client.get("/users/", {}, HTTP_AUTHORIZATION='JWT {}'.format(token), format='json')
        self.assertIn(email, [i['email'] for i in response.data], msg=response.data)
