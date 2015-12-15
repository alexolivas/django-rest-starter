from models import SystemPreferences
from rest_framework import serializers


class SystemPreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemPreferences
        exclude = ('id', 'created_date', 'updated_date')
