from django.contrib import admin
from models import UserPreferences
from models import Client
from models import ClientMembership


class UserAccountSetupAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user__is_active', 'created_date', 'updated_date')
    # exclude = ('user_permissions', 'last_login', 'date_joined')
admin.site.register(UserPreferences, UserAccountSetupAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'active')
    list_filter = ('name', 'state', 'active')
admin.site.register(Client, ClientAdmin)


admin.site.register(ClientMembership)
