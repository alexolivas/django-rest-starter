from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date',)
