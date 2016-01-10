from django.conf.urls import include, url
from django.contrib import admin
from accounts import urls_all_users, urls_staff_users
from rest_framework import routers
from authentication import auth_urls

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/auth/', include(auth_urls)),
    url(r'^v1/user/', include(urls_all_users)),
    url(r'^v1/users/', include(urls_staff_users)),

    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Django REST Skeleton Administration'
