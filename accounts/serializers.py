from django.contrib.auth.models import User
from models import UserPreferences
# from accounts.models import Client, ClientMembership
from rest_framework import serializers


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ('id', 'name')
#         read_only_fields = ('created_date', 'updated_date')


class UserDetailsSerializer(serializers.Serializer):
    id = serializers.UUIDField()


# This view contains basic user information
class UserBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'groups', 'user_permissions')


# This view contains more information that admin user's can view
class UserDetailedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        exclude = ('id', 'user', 'created_date', 'updated_date')
