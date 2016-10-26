from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import ProfileDetail

urlpatterns = [
    url(r'^$', ProfileDetail.as_view(), name='profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
