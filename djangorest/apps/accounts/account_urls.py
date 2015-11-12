from django.conf.urls import url
from djangorest.apps.accounts import views
from rest_framework.urlpatterns import format_suffix_patterns

# TODO Change these to the real account views i.e. user_views, account_views
# TODO What I am working on here is only needed for the CELLA project i.e. adding user_views, user_urls etc
# TODO In CELLA create a new app called clients, users can belong to 1 or more clients (ManyToMany or OneToMany??)
urlpatterns = [
    url(r'^', views.AccountList.as_view(), name='account'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view(), name='profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
