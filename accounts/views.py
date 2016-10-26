from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import Http404
from models import Account
from serializers.account_serializer import AccountSerializer


class AccountDetails(APIView):
    """
    This endpoint allows a user to manage their account details.
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (AnonRateThrottle,)

    @staticmethod
    def get_account_details(user_id):
        try:
            return Account.objects.get(user__pk=user_id)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        account = self.get_account_details(request.user.id)
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(dict(), status=status.HTTP_200_OK)
