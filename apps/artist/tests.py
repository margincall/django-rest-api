from django.test import TestCase

from rest_framework.test import APITestCase

from apps.artist.models import Artist


class ArtistModelTests(TestCase):

    def test_Artist_생성_및_문자열_표현_확인(self):
        nickname = 'Nirvana'
        artist = Artist.objects.create(nickname=nickname)
        self.assertEqual(str(artist), nickname)


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
