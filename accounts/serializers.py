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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'groups', 'user_permissions')


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        exclude = ('id', 'user', 'created_date', 'updated_date')
