from django.contrib.auth.models import User
from models import UserPreferences
from accounts.models import Client, ClientMembership
from rest_framework import serializers


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ('id', 'name')
#         read_only_fields = ('created_date', 'updated_date')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     # client = ClientSerializer(many=True)
#     # is_admin = serializers.SerializerMethodField()
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'date_joined')
#
#
# class ClientMemberSerializer(serializers.ModelSerializer):
#     client = ClientSerializer()
#
#     class Meta:
#         model = ClientMembership
#         read_only_fields = ('created_date', 'updated_date')


class UserPreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPreferences
        exclude = ('id', 'user', 'created_date', 'updated_date')
        # fields = ('date_format', 'time_format', 'client', 'is_client')
        # fields = ('client', 'is_admin', 'date_format', 'time_format')

# TODO: Create a user group serializer that returns booleans
# class UserGroupSerializer(serializers.Serializer):
#     name = C
#
#




# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
        # fields = ('name', 'address_1', 'address_2', 'city', 'state', 'primary_phone')

#
# class TokenSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = Token
#         fields = ('key', 'user')
