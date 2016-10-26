from rest_framework import serializers
from accounts.models import Account
from user_serializer import UserSerializer


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ('user', 'bio', 'location', 'birth_date',)
