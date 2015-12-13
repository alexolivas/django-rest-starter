from rest_framework import generics
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from serializers import UserSettingsSerializer
# from models import UserProfile


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
