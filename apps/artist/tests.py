from django.test import TestCase

from apps.artist.models import Artist


class ArtistModelTests(TestCase):

    def test_Artist_생성_및_문자열_표현_확인(self):
        nickname = 'Nirvana'
        artist = Artist.objects.create(nickname=nickname)
        self.assertEqual(str(artist), nickname)
