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

    def test_User_에_nickname_제대로_부여되는지_확인(self):
        user = User.objects.create_user('panic@the.disco', 'password')
        user.nickname = 'my_nickname'
        user.save()
        self.assertEqual('my_nickname', User.objects.get(email='panic@the.disco').nickname)


class UserAPITests(APITestCase):

    def setUp(self):
        # JWT Authentication
        User.objects.create_user(email='email@email.com', password='password')
        response = self.client.post(reverse('obtain_jwt_token'),
                                    {'email': 'email@email.com', 'password': 'password'},
                                    format='json')
        self.token = response.data['token']

    def test_API_에서_생성된_User_객체를_받아오는지_확인(self):
        email = 'green@day.com'
        User.objects.create_user(email=email, password='password')

        response = self.client.get('/users/', {}, HTTP_AUTHORIZATION='JWT {}'.format(self.token), format='json')
        self.assertIn(email, [i['email'] for i in response.data], msg=response.data)

    def test_API_에서_nickname_받아오는지_확인(self):
        email = 'cold@play.com'
        user = User.objects.create_user(email=email, password='password')
        user.nickname = 'Viva La Vida'
        user.save()

        response = self.client.get('/users/', {}, HTTP_AUTHORIZATION='JWT {}'.format(self.token), format='json')
        self.assertIn('Viva La Vida', [i['nickname'] for i in response.data if i['email'] == email], msg=response.data)
