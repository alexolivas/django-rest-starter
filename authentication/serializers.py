from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserMetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined')


class TokenSerializer(serializers.ModelSerializer):
    user = UserMetadataSerializer()

    class Meta:
        model = Token
        exclude = ('created',)
