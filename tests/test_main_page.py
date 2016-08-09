from django.test import Client, LiveServerTestCase
from rest_framework import status


class MainPageFunctionalTests(LiveServerTestCase):
    def test_Main_Page_HTTP_200_OK(self):
        url = self.live_server_url
        response = Client().get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response)
