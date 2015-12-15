from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from serializers import UserDetailsSerializer
from system.models import SystemPreferences
from system.serializers import SystemPreferencesSerializer
from accounts.models import User, UserPreferences
from accounts.serializers import UserPreferencesSerializer


# TODO: Separate serializers into get_serializers, post_serializers, delete_serializers OR outbound and inbound


class UserDetails(APIView):
    """
    This endpoint provides any user an interface to manage their own account's details.

    * Uses token authentication.
    * Requires user to be authenticated.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # TODO: Get the user details
        user = self.request.user
        print user
        if user is not None:
            user_data = User.objects.get(user=user)
            serializer = UserDetailsSerializer(user_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User data not in the request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        # TODO: Update the user's details
        user = self.request.user
        print user
        if user is not None:
            user_data = User.objects.get(user=user)
            serializer = UserDetailsSerializer(user_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User data not in the request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserPreferencesView(APIView):
    """
    This endpoint gets a user's preferences, if the user has not set any the default
    system preferences will be returned.

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (AnonRateThrottle,)

    def get(self, request, format=None):
        if request.user and request.user.pk:
            print request.user
            try:
                # Grab the user by email, once we have the user we will pass in the username
                # to django's built in authentication system
                user_details = UserPreferences.objects.get(user=request.user.pk)

                print user_details
                print user_details.client.all()
                print user_details.date_format
                print user_details.time_format

                # Serialize the user's details, including their preferences and roles
                serializer = UserPreferencesSerializer(user_details)

                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserPreferences.DoesNotExist:
                # The user has not is not overriding the default system preferences, grab them
                print 'no user preferences, getting the default system preferences'
                system_prefs = SystemPreferences.objects.all()[0]
                print system_prefs
                serializer = SystemPreferencesSerializer(system_prefs)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {
                'message': 'Unable to find user in the request'
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(APIView):
    """
    This endpoint provides any user an interface to upload files to their account

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