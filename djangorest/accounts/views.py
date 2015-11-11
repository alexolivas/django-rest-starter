# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status

# class CreateAccountView(APIView):
#     """
#     This endpoint creates a tenant specific SFTP account for the Seapig datapump.<br/>
#     * Requires token authentication
#     """
# authentication_classes = (TokenAuthentication,)
# permission_classes = (IsAuthenticated,)
#
# def post(self, request, format=None):
#     return Response({
#         'success': 'true',
#         'message': 'Seapig SFTP account successfully created for ' + tenant
#     })

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from djangorest.accounts.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

