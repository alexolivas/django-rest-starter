from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
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

    def __unicode__(self):
        return self.name


class UserAccountSetup(models.Model):
    user = models.OneToOneField(User, unique=True)
    client = models.ManyToManyField(Client, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    # TODO ##########################################
    # TODO ##########################################
    # TODO: Remove the client and user app
    # TODO ##########################################
    # TODO ##########################################

    class Meta:
        verbose_name = 'User Account Setup'
        verbose_name_plural = 'User Account Setup'

    def __unicode__(self):
        return self.user.email


# TODO: We don't necessarily need to return all data with one API call, we can make the UI make 2 calls
# This is where we could potentially add user specific settings i.e. timezone preference, custom date format, language
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, unique=True)
#
#     class Meta:
#         verbose_name = 'User Profile'
#         verbose_name_plural = 'User Profiles'
#
#     def __unicode__(self):
#         return self.user.email
