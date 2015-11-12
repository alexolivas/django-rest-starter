from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from djangorest.apps.authentication import auth_urls
from djangorest.apps.accounts import account_urls

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/auth/', include(auth_urls)),
    url(r'^v1/accounts/', include(account_urls)),
    # url(r'^api-token-auth/', views.obtain_auth_token), # Automatically gets or generates new token
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Gives Login Access to the Webapp
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Django REST Skeleton Administration'
