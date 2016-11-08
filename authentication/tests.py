from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt import utils
from django.contrib.auth.models import User


class BaseAuthTestCase(TestCase):

    def setUp(self):
        """
        Create a user which will be used for all tests in this suite
        :return:
        """
        self.username = 'testuser'
        self.password = 'secretpass'
        self.email = 'fakeaccount@email.com'
        test_user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
        )


class LoginTestCase(BaseAuthTestCase):

    # Follow: https://docs.djangoproject.com/en/1.10/topics/testing/advanced/#testing-reusable-applications

    def setUp(self):
        self.api_client = APIClient()
        return super(LoginTestCase, self).setUp()

    def test_jwt_auth(self):
        """
        This test verifies that an existing user can get an auth token using a JSON post
        :return:
        """
        login_credentials = {
            'username': self.username,
            'password': self.password
        }
        response = self.api_client.post('/auth/api-token-auth/', login_credentials, format='json')
        jwt_token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(jwt_token)

        decoded_payload = utils.jwt_decode_handler(jwt_token)
        self.assertEqual(decoded_payload['username'], self.username)
        self.assertEqual(decoded_payload['email'], self.email)

    def test_invalid_jwt_auth(self):
        """
        This test verifies that using a JSON post, an auth token cannot be obtained, if invalid
        user credentials are used to obtain one
        :return:
        """
        login_credentials = {
            'username': self.username,
            'password': 'aninvalidpassword'
        }
        response = self.api_client.post('/auth/api-token-auth/', login_credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
