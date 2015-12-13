from django.contrib.auth.models import User
from models import UserAccountSetup
from accounts.models import Client
from rest_framework import serializers
from authentication.serializers import TokenSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'groups')


class UserAccountSetupSerializer(serializers.Serializer):
    user = UserSerializer()
    client = ClientSerializer()
    # token = TokenSerializer()

    class Meta:
        # model = UserAccount
        fields = ('user', 'client')


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
