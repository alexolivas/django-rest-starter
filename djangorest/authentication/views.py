from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


class LoginView(APIView):
    """
    This endpoint generates a new token effectively granting a user access to the system

    * This API doesn't require authentication or permission
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format=None):
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Use django's built in authentication
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # TODO: this is not JSON serializable > fixed by creating a serializable object
                    # serializer_class = UserSerializer
                    # TODO: Get the user's token, if one doesn't exist, create it (see below)
                    # new_token = Token.objects.create(user=request.user)
                    # user_token = Token.objects.get(user=user)
                    message = {'message': 'Welcome!'}
                    return Response(message, status=status.HTTP_200_OK)
                else:
                    message = {'message': 'Account has been disabled.'}
                    return Response(message, status=status.HTTP_401_UNAUTHORIZED)
            else:
                message = {'message': 'Bad login credentials.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        message = {'message': 'Missing username and/or password.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    This endpoint revokes a user's token effectively revoking their access to the system

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (permissions.IsAdminUser,)

    # def post(self, request, format=None):
    def post(self, request, format=None):
        # TODO: Get the token based on the user ID and delete it so that it is no longer valid
        # TODO: Add null checks around this
        user_token = Token.objects.get(user=request.user.pk)
        message = {
            'success': 'true',
            'message': 'Everything is ok!',
            'user': user_token.key
        }
        return Response(message, status=status.HTTP_200_OK)
