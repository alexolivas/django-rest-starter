from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)
    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=150, blank=True)
    primary_phone = models.CharField(max_length=25, blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'client'

    def __unicode__(self):
        return self.name


class UserPreferences(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    user = models.OneToOneField(User, unique=True)
    date_format = models.CharField(max_length=25, default='M/dd/yyyy')
    time_format = models.CharField(max_length=25, default='HH:mm:ss')

    class Meta:
        verbose_name = 'User Preferences'
        verbose_name_plural = 'User Preferences'
        db_table = 'user_preferences'

    def __unicode__(self):
        return self.user.email


class ClientMembership(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    user = models.OneToOneField(User, unique=True)
    client = models.OneToOneField(Client, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'client_membership'

    def __unicode__(self):
        return self.user.email
