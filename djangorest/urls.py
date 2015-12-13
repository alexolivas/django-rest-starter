from django.conf.urls import include, url
from django.contrib import admin
from accounts import user_urls
from rest_framework import routers

from authentication import auth_urls
from admin import admin_urls

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/auth/', include(auth_urls)),
    url(r'^v1/users/', include(user_urls)),
    # url(r'^v1/admin/', include(admin_urls)),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Gives Login Access to the Webapp
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Django REST Skeleton Administration'
