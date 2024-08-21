from django.test import TestCase
from django.urls import reverse
from django.test import Client

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_response(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)