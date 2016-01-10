from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from serializers import UserBasicInfoSerializer, UserDetailedInfoSerializer
from system.models import SystemPreferences
from system.serializers import SystemPreferencesSerializer
from models import UserPreferences
from serializers import UserPreferencesSerializer
from system.permissions import ManageUsersPermission


class MyProfile(APIView):
    """
    This endpoint provides users an interface to manage their own account's details.

    * Uses token authentication.
    * Requires user to be authenticated.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.user
        if user is not None:
            serializer = UserBasicInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User data not in the request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
    #     # TODO: Update the user's details
    #     user = self.request.user
    #     print user
    #     if user is not None:
    #         user_data = User.objects.get(user=user)
    #         serializer = UserDetailsSerializer(user_data)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         message = {'message': 'User data not in the request.'}
    #         return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    """
    This endpoint provides an interface for users with the "manage users" permission
    to manage user account details.

    * Uses token authentication.
    * Requires user to be authenticated.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, ManageUsersPermission)

    def get(self, request, format=None):
        user = self.request.user
        if user is not None:
            serializer = UserDetailedInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User data not in the request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserPreferencesView(APIView):
    """
    This endpoint gets a user's preferences, if the user has not set any the default
    system preferences will be returned.

    * Uses token authentication.
    * Requires user to be authenticated.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        if request.user and request.user.pk:
            print request.user
            try:
                # Get the user's preferences and serialize the data
                user_details = UserPreferences.objects.get(user=request.user.pk)
                serializer = UserPreferencesSerializer(user_details)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserPreferences.DoesNotExist:
                # The user is not overriding the default system preferences, grab them
                system_prefs = SystemPreferences.objects.all()[0]
                serializer = SystemPreferencesSerializer(system_prefs)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {
                'message': 'Unable to find user in the request'
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(APIView):
    """
    This endpoint provides any user an interface to upload files to their client account. These files
    will be visible to all other members of the client account as well as staff and admin users.

    * Uses token authentication.
    * Requires user to be authenticated.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)