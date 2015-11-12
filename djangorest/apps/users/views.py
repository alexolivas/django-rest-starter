from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
# from serializers import TokenSerializer
# TODO: Create a util class that helps with all these functions


class EditProfileView(APIView):
    """
    This endpoint provides a user an interface to edit their own information

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        message = {
            'message': 'Unable to find user in the request'
        }
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateUserView(APIView):
    """
    This endpoint provides an admin user an interface to create a new user in the system

    * Requires token authentication.
    * Requires user to be an admin
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, format=None):

        message = {
            'message': 'Unable to find user in the request'
        }
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditUserView(APIView):
    """
    This endpoint provides an admin user access to edit any other users in the system.

    * Requires token authentication.
    * Requires user to be an admin
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, format=None):

        message = {
            'message': 'Unable to find user in the request'
        }
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteUserView(APIView):
    """
    This endpoint provides an admin user access to inactivate a user from the system.

    * Requires token authentication.
    * Requires user to be an admin
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, format=None):

        message = {
            'message': 'Unable to find user in the request'
        }
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
