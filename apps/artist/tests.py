from django.test import TestCase

from rest_framework.test import APITestCase

from apps.artist.models import Artist


class ArtistModelTests(TestCase):

    def test_Artist_생성_및_문자열_표현_확인(self):
        nickname = 'Nirvana'
        artist = Artist.objects.create(nickname=nickname)
        self.assertEqual(str(artist), nickname)


class ArtistAPITests(APITestCase):

    def test_API_에서_생성된_Artist_객체를_받아오는지_확인(self):
        nickname = 'Oasis'
        self.artist = Artist.objects.create(nickname=nickname)

        response = self.client.get("/artists/", {}, format='json')
        self.assertIn({'nickname': nickname}, response.data, msg=response.data)
