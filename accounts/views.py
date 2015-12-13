from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from serializers import UserSerializer, UserSettingsSerializer
# from models import UserSettings


# class UserAccountDetails(generics.RetrieveAPIView):
#     """
#     This endpoint provides any user an interface to view their account's details.
#
#     * Requires token authentication.
#     """
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     serializer = UserAccountSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return UserProfile.objects.get(user=user)
# class UserLoginDetails(APIView):
#     """
#     This endpoint provides any user an interface to get their basic information, including first name,
#     last name, email, username, client names, and roles.
#
#     * Requires token authentication.
#     """
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, format=None):
#         user = self.request.user
#         if user is not None:
#             user_data = UserAccount.objects.get(user=user)
#             serializer = UserAccountSerializer(user_data)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             message = {'message': 'User data not in the request.'}
#             return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserAccountDetails(APIView):
    """
    This endpoint provides any user an interface to view their account's basic details.

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # TODO: Rename the User Settings table to User Admin Settings (for admin only settings or leave it the same?)
        # TODO: Create a User Profile table for a user's profile setting i.e. timezone, date format, etc (needed?)
        # TODO: combine both result sets then the serializer should take care of it
        # TODO: If I do split them, then this API should be called something else to be only used after login
        # TODO: Add audit fields to all these tables so that I know what is being change,
        # TODO:     in fact, create an auditable table and extend it to all the tables that I want to be audited
        user = self.request.user
        if user is not None:
            try:
                user_settings = UserSettings.objects.get(user=user)
                serializer = UserSettingsSerializer(user_settings)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserSettings.DoesNotExist:
                # This user does not have custom settings, simply get the user's details
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User data not in the request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
