from models import SystemPreferences
from rest_framework import serializers


class SystemPreferencesSerializer(serializers.ModelSerializer):
    # is_staff = serializers.SerializerMethodField()
    # is_admin = serializers.SerializerMethodField()

    class Meta:
        model = SystemPreferences
        exclude = ('id', 'created_date', 'updated_date')
