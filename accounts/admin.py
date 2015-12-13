from django.contrib import admin
from models import UserAccountSetup
from models import Client


class UserAccountSetupAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('client__name', 'user__is_active')
    # exclude = ('user_permissions', 'last_login', 'date_joined')
admin.site.register(UserAccountSetup, UserAccountSetupAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'active')
    list_filter = ('name', 'state', 'active')
admin.site.register(Client, ClientAdmin)
