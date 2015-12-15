from rest_framework.authtoken.models import Token
from rest_framework import serializers
from accounts.models import Client, User, ClientMembership


class ClientMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')
        read_only_fields = ('created_date', 'updated_date')


class UserMetadataSerializer(serializers.ModelSerializer):
    is_staff = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_admin')

    def get_is_staff(self, user):
        if user.is_superuser:
            # Ignore this logic if the user is an admin
            return False
        else:
            is_staff = False
            for group in user.groups.all():
                print str(group.name).lower()
                if str(group.name).lower() == 'staff':
                    is_staff = True
                    break
            return is_staff

    def get_is_admin(self, user):
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
