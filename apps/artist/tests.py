from django.test import TestCase

from rest_framework.test import APITestCase

from apps.artist.models import Artist
from apps.authentication.models import User


class ArtistModelTests(TestCase):

    def test_Artist_생성_및_문자열_표현_확인(self):
        nickname = 'Nirvana'
        artist = Artist.objects.create(nickname=nickname)
        self.assertEqual(str(artist), nickname)

    def test_Artist_에_User_외부키_부여(self):
        user = User.objects.create_user('artist@email.com', 'password')
        artist = Artist.objects.create(nickname='artist_name')
        artist.user = user
        artist.save()
        self.assertEqual(user, Artist.objects.get(nickname='artist_name').user)

    def test_Artist_에_연결된_User_삭제(self):
        user = User.objects.create_user('will_delete@email.com', 'password')
        artist = Artist.objects.create(nickname='artist_name')
        artist.user = user
        artist.save()

        user.delete()
        self.assertIsNone(Artist.objects.get(nickname='artist_name').user)


class ArtistAPITests(APITestCase):
    def test_CREATE_Artist(self):
        self.client.post("/artists/", {'nickname': 'Deep Purple'}, format='json')
        self.assertIn('Deep Purple', [i.nickname for i in Artist.objects.all()])

    def test_READ_Artist(self):
        nickname = 'Oasis'
        Artist.objects.create(nickname=nickname)

        response = self.client.get("/artists/", {}, format='json')
        self.assertIn({'nickname': nickname}, response.data, msg=response.data)

    def test_UPDATE_Artist(self):
        artist = Artist.objects.create(nickname='before_nickname')

        self.client.put('/artists/' + str(artist.pk) + '/', {'nickname': 'new_nickname'}, format='json')
        self.assertEqual('new_nickname', Artist.objects.get(pk=artist.pk).nickname)

    def test_DELETE_Artist(self):
        artist = Artist.objects.create(nickname='My Chemical Romance')
        self.client.delete('/artists/' + str(artist.pk) + '/', {}, format='json')

        self.assertNotIn('My Chemical Romance', [i.nickname for i in Artist.objects.all()])
