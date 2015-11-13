from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from serializers import AccountSerializer


class AccountDetail(APIView):
    """
    This endpoint provides a user an interface to manage their own account's profile information.

    * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # Get user account details
        snippet = self.get_object(pk)
        serializer = AccountSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # Update fields on the account and save
        snippet = self.get_object(pk)
        serializer = AccountSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountList(APIView):
    """
    This endpoint provides an admin user an interface to manage user accounts in their system.

    * Requires token authentication.
    * Requires user to be an admin
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request, format=None):
        # TODO: Implement options to only return certain users
        users = User.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
