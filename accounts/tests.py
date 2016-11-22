from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt import utils
from django.contrib.auth.models import User
from accounts.models import Profile


class BaseAuthTestCase(TestCase):

    def setUp(self):
        """
        Create a user and their profile which will be used for all tests in this suite
        :return:
        """
        self.username = 'testuser'
        self.password = 'secretpass'
        self.email = 'fakeaccount@email.com'
        self.first_name = 'Test'
        self.last_name = 'User'
        test_user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )

        profile = Profile.objects.create(
            user=test_user,
            bio="Lorem Ipsum...",
            location="79936",
            birth_date="1985-01-07"
        )


class LoginTestCase(BaseAuthTestCase):

    def setUp(self):
        self.api_client = APIClient()
        return super(LoginTestCase, self).setUp()

    def test_unauthorized_view_fails(self):
        """
        This test verifies that un-authenticated requests to accounts endpoints fail
        :return:
        """
        response = self.api_client.get('/account/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_view_your_profile_with_jwt_token(self):
        """
        This test verifies that an existing user can view their profile page when authenticated
        with a valid JWT Token
        :return:
        """
        print "inside test_view_your_profile"
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

        # That comes down to the design of your program. At some point you will issue a request to get the token.
        # On receiving the response, your client could just set a timer to pop just before the expiration time and
        # use the callback to issue the refresh.
        # https://github.com/auth0/auth0-angular/blob/master/docs/refresh-token.md
        # https://github.com/auth0-samples/auth0-angularjs-sample
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + jwt_token)
        response = self.api_client.get('/account/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profile = response.json()['profile']
        self.assertIsNotNone(profile)
        self.assertEqual(profile['birth_date'], '1985-01-07')
        self.assertEqual(profile['location'], '79936')

        # Logout of the application and verify that you can no longer see your account's details
        self.api_client.logout()
        response = self.api_client.get('/account/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_jwt_auth(self):
        """
        This test verifies that the accounts endpoint returns an un-authorized response when it
        receives a request with an invalid token
        :return:
        """
        login_credentials = {
            'username': self.username,
            'password': 'aninvalidpassword'
        }
        response = self.api_client.post('/auth/api-token-auth/', login_credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_without_a_profile(self):
        """
        This test verifies that the system robustly handles a user that never created a profile
        attempting to view their profile.
        :return:
        """
        # Create a new user, but don't create a profile
        rafa_username = 'rafa.marquez'
        rafa_password = 'bestdefenderever'
        email = 'rafa.marquez@email.com'
        rafa = 'Rafa'
        marquez = 'Marquez'
        user_without_profile = User.objects.create_user(
            username=rafa_username,
            password=rafa_password,
            email=email,
            first_name=rafa,
            last_name=marquez
        )

        login_credentials = {
            'username': rafa_username,
            'password': rafa_password
        }
        response = self.api_client.post('/auth/api-token-auth/', login_credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        jwt_token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(jwt_token)

        decoded_payload = utils.jwt_decode_handler(jwt_token)
        self.assertEqual(decoded_payload['username'], rafa_username)
        self.assertEqual(decoded_payload['email'], email)

        # Verify the response returned is 404 (NOT FOUND)
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + jwt_token)
        response = self.api_client.get('/account/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
