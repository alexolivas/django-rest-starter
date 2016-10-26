from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class AccountDetails(APIView):
    """
    This endpoint allows a user to manage a release: view, edit, delete.

    * Requires Token authentication.
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (AnonRateThrottle,)
    # serializer_class = LoginSerializer

    # def get_serializer_class(self):
    #     return self.serializer_class

    def get(self, request, format=None):
        return Response(dict(), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(dict(), status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        return Response(dict(), status=status.HTTP_200_OK)