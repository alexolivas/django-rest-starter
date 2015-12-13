from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^', views.AccountList.as_view(), name='account'),
    # url(r'^profile/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view(), name='profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
