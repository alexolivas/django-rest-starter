from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from system.permissions import ManageUsersPermission
from serializers import UserBasicInfoSerializer, UserDetailedInfoSerializer


class UserSearch(APIView):
    """
    This endpoint provides users with the user's list permission an interface to search for client users

    * Uses token authentication.
    * Requires user to be authenticated.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, ManageUsersPermission)
    serializer_class = UserBasicInfoSerializer

    def get(self, request, format=None):
        print 'inside user search...'
        user = self.request.user
        if user is not None:
            serializer = UserBasicInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User data not in the request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


# TODO: I need to define what a regular user is and what a staff user is
# TODO: Regular user: client? staff: factory worker?
# class UserAccountSearch(generics.ListAPIView):
#     """
#     This endpoint provides a staff user an interface to search for users associated their client
#
#     * Requires token authentication.
#     * Requires user to be an admin
#     """
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)  # Make this a staff only permission
#     serializer_class = UserAccountSerializer
#
#     # queryset = UserAccount.objects.all()
#     serializer = UserAccountSerializer
#     filter_backends = (filters.SearchFilter,)
#     # search_fields = ('username', 'email', 'active')
#     search_fields = ('client__name', 'active')
#
#     def get_queryset(self):
#         # This is using "Filtering against the URL"
#         user = self.request.user
#         return UserProfile.objects.filter(client=user.client)
