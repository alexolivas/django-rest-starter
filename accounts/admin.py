from django.contrib import admin
from models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # list_display = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'user__is_active')
    list_filter = ('user__is_active',)
    search_fields = ['user__email', 'user__first_name', 'user__last_name']

admin.site.register(Profile, ProfileAdmin)