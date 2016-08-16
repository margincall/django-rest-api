from django.test import Client, LiveServerTestCase
from rest_framework import status


class MainPageFunctionalTests(LiveServerTestCase):
    def test_Main_Page_인증되지_않은_요청_HTTP_401_UNAUTHORIZED(self):
        url = self.live_server_url
        response = Client().get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response)
