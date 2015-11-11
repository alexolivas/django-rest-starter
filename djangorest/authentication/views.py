from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from serializers import TokenSerializer
from django.core.exceptions import ObjectDoesNotExist


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
                    try:
                        # Get the user's existing token, if one doesn't exist generate a new one
                        user_token = Token.objects.get(user=user)
                    except ObjectDoesNotExist:
                        user_token = Token.objects.create(user=user)

                    # Serialize the user and token so the data can be passed back to the caller
                    serializer = TokenSerializer(user_token)
                    if serializer.is_valid():
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        # Something went wrong with the serialization, return 500 error
                        return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
