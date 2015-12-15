from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from serializers import TokenSerializer, ClientMemberSerializer
from accounts.models import ClientMembership, UserPreferences
from accounts.serializers import UserPreferencesSerializer
from system.models import SystemPreferences
from system.serializers import SystemPreferencesSerializer


class LoginView(APIView):
    """
    This endpoint generates a new token effectively granting a user access to the system

    * This API doesn't require authentication or permission
    """
    authentication_classes = ()
    permission_classes = ()
    throttle_classes = (AnonRateThrottle,)

    def post(self, request, format=None):
        """
        username -- A first parameter
        password -- A second parameter
        parameters:
            - username: username
              description: user's email address
              required: true
              type: string
              paramType: form
            - password: password
              description: user's password
              required: true
              type: string
        """
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # We are using email as the username, authenticate with that instead of the username
            user = self.authenticate_by_email(username, password)
            if user is not None:
                # print 'is user active: ' + user.is_active
                if user.is_active:
                    # Get the user's existing token, if one doesn't exist generate a new one
                    user_token, created = Token.objects.get_or_create(user=user)

                    results = dict()

                    # Serialize the user and token so the data can be passed back to the caller
                    token_serializer = TokenSerializer(user_token)
                    results['token'] = token_serializer.data['key']
                    results['user'] = token_serializer.data['user']

                    # Determine if the user is part of a client cohort
                    client_membership = self.get_client_membership(user)
                    if client_membership is not None:
                        client_membership_serializer = ClientMemberSerializer(client_membership)
                        results['client'] = client_membership_serializer.data['client']

                    # Get the user or system preferences
                    user_prefs = self.get_user_preferences(user)
                    if user_prefs is not None:
                        results['preferences'] = user_prefs
                    else:
                        # Default System Preferences have not been setup
                        message = {'message': 'The default System Preferences have not been setup.'}
                        return Response(message, status=status.HTTP_412_PRECONDITION_FAILED)

                    return Response(results, status=status.HTTP_200_OK)
                else:
                    # This user is not active in the system
                    message = {'message': 'This account is inactive.'}
                    return Response(message, status=status.HTTP_401_UNAUTHORIZED)
            else:
                # Incorrect username/password combination
                message = {'message': 'Invalid credentials.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        message = {'message': 'Missing username and/or password.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def authenticate_by_email(email, password):
        # We are using an email as the username, so we can't use django's built in authentication,
        # Let's authenticate by grabbing the user by email and checking the password
        try:
            # Grab the user by email, once we have the user we will pass in the username
            # to django's built in authentication system
            user_details = User.objects.get(email=email)

            # Use django's built in authentication
            user = authenticate(username=user_details.username, password=password)

            if user is not None:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_client_membership(user):
        try:
            return ClientMembership.objects.get(user=user, active=True)
        except ClientMembership.DoesNotExist:
            return None

    @staticmethod
    def get_user_preferences(user):
        try:
            # Get the user's custom preferences
            user_prefs = UserPreferences.objects.get(user=user)
            user_prefs_serializer = UserPreferencesSerializer(user_prefs)
            return user_prefs_serializer.data
        except UserPreferences.DoesNotExist:
            # The user has not setup custom preferences, get the default system preferences
            try:
                # System preferences are setup initially, it's a unique record so there should only be 1
                # record at all times. Place in a try/catch for robustness
                sys_prefs = SystemPreferences.objects.all()[0]
                sys_prefs_serializer = SystemPreferencesSerializer(sys_prefs)
                return sys_prefs_serializer.data
            except SystemPreferences.DoesNotExist:
                return None


class LogoutView(APIView):
    """
    This endpoint revokes a user's token effectively revoking their access to the system

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        if request.user and request.user.pk:
            # No need to check if token exists because the user would not be able to call
            # this endpoint if a token did in fact not exist
            user_token = Token.objects.get(user=request.user.pk)
            user_token.delete()
            message = {
                'message': 'Successfully logged out'
            }
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {
                'message': 'Unable to find user in the request'
            }
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
