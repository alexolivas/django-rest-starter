from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import Http404
from models import Profile
from serializers.user_serializer import UserSerializer
from serializers.profile_serializer import ProfileSerializer


class AccountDetails(APIView):
    """
    This endpoint allows a user to manage their account details.
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (AnonRateThrottle,)

    @staticmethod
    def get_user_profile(user_id):
        try:
            return Profile.objects.get(user__pk=user_id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        profile = self.get_user_profile(request.user.id)
        user_serializer = UserSerializer(profile.user)
        profile_serializer = ProfileSerializer(profile)
        account_data = {
            'user': user_serializer.data,
            'profile': profile_serializer.data
        }
        return Response(account_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(dict(), status=status.HTTP_200_OK)
