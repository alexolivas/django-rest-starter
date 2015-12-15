from django.contrib import admin
from models import UserPreferences
from models import Client
from models import ClientMembership


class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user__is_active', 'created_date', 'updated_date')
admin.site.register(UserPreferences, UserPreferencesAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'active')
    list_filter = ('name', 'state', 'active')
admin.site.register(Client, ClientAdmin)


class ClientMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'active')
    list_filter = ('client', 'active')
admin.site.register(ClientMembership, ClientMembershipAdmin)
