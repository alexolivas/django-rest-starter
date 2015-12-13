from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from django.contrib.auth import authenticate
from accounts.models import UserAccountSetup
from serializers import TokenSerializer


class LoginView(APIView):
    """
    This endpoint generates a new token effectively granting a user access to the system

    * This API doesn't require authentication or permission
    """
    authentication_classes = ()
    permission_classes = ()
    throttle_classes = (AnonRateThrottle,)

    def post(self, request, format=None):
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # We are using email as the username, authenticate with that instead of the username
            user_account = self.authenticate_by_email(username, password)
            if user_account is not None:
                # print 'is user active: ' + user.is_active
                if user_account.user.is_active:

                    # TODO: I'm going to split up the login into 2 steps, 1 for authentication to get the key
                    # TODO: and 2 once I get the key I will get the user's basic details

                    # Get the user's existing token, if one doesn't exist generate a new one
                    user_token, created = Token.objects.get_or_create(user=user_account.user)

                    # Serialize the user and token so the data can be passed back to the caller
                    serializer = TokenSerializer(user_token)

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    # This user is not active in the system
                    message = {'message': 'Account has been disabled.'}
                    return Response(message, status=status.HTTP_401_UNAUTHORIZED)
            else:
                # Incorrect username/password combination
                message = {'message': 'Invalid credentials.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        message = {'message': 'Missing username and/or password.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def authenticate_by_email(self, email, password):
        # We are using an email as the username, so we can't use django's built in authentication,
        # Let's authenticate by grabbing the user by email and checking the password
        try:
            # Grab the user by email, once we have the user we will pass in the username
            # to django's built in authentication system
            user_account = UserAccountSetup.objects.get(user__email=email)

            # Use django's built in authentication
            user = authenticate(username=user_account.user.username, password=password)

            if user is not None:
                return user_account
            else:
                return None
        except UserAccountSetup.DoesNotExist:
            # TODO: Return JSON that front-end can read?
            print 'User Account not setup for login'
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
