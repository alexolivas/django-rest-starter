from django.contrib import admin
from models import SystemPreferences


class SystemPreferencesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = SystemPreferences.objects.all().count()
        if count == 0:
            return True
        return False
admin.site.register(SystemPreferences, SystemPreferencesAdmin)