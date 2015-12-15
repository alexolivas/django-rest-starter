from django.db import models


class SystemPreferences(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    date_format = models.CharField(max_length=25, default='M/dd/yyyy')
    time_format = models.CharField(max_length=25, default='HH:mm:ss')

    class Meta:
        verbose_name = 'System Preferences'
        verbose_name_plural = 'System Preferences'
        db_table = 'system_preferences'

    def __unicode__(self):
        return str(self.id)
