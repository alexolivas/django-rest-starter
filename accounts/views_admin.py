# from rest_framework import generics
# from rest_framework import filters
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from serializers import UserAccountSerializer
# from models import UserAccount
#
#
# class UserAccountSearch(generics.ListAPIView):
#     """
#     This endpoint provides an admin user an interface to search for user users
#
#     * Requires token authentication.
#     * Requires user to be an admin
#     """
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated, IsAdminUser)
#     queryset = UserAccount.objects.all()
#     serializer = UserAccountSerializer
#     filter_backends = (filters.SearchFilter,)
#     # search_fields = ('username', 'email', 'active')
#     search_fields = ('client__name', 'active')
#
#
# class UserAccountDetails(generics.RetrieveAPIView):
#     """
#     This endpoint provides an admin user an interface to view any user account's details
#
#     * Requires token authentication.
#     * Requires user to be an admin
#     """
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated, IsAdminUser)
#     serializer_class = UserAccountSerializer
#
#     def get_queryset(self):
#         # This is using "Filtering against the URL"
#         user_id = self.kwargs['id']
#         return UserAccount.objects.get(pk=user_id)
