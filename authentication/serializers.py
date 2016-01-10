from rest_framework.authtoken.models import Token
from rest_framework import serializers
from accounts.models import Client, User, ClientMembership


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ClientMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')
        read_only_fields = ('created_date', 'updated_date')


class UserMetadataSerializer(serializers.ModelSerializer):
    is_warehouse_employee = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_warehouse_employee', 'is_admin')

    @staticmethod
    def get_is_warehouse_employee(user):
        if user.is_superuser:
            # Ignore this logic if the user is an admin
            return False
        else:
            is_warehouse_employee = False
            for group in user.groups.all():
                if str(group.name).lower() == 'warehouse employees':
                    is_warehouse_employee = True
                    break
            return is_warehouse_employee

    @staticmethod
    def get_is_admin(user):
        # If they are superusers then they are admins by default
        return user.is_superuser


class ClientMemberSerializer(serializers.ModelSerializer):
    client = ClientMetadataSerializer()

    class Meta:
        model = ClientMembership
        read_only_fields = ('created_date', 'updated_date')


class TokenSerializer(serializers.ModelSerializer):
    user = UserMetadataSerializer()

    class Meta:
        model = Token
        exclude = ('created',)
