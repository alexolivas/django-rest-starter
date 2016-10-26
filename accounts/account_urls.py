from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import AccountDetails

urlpatterns = [
    url(r'^$', AccountDetails.as_view(), name='account'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
