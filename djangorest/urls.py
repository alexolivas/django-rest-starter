from django.conf.urls import include, url
from django.contrib import admin
# from rest_framework import routers
from authentication import auth_urls
from profiles import profile_urls

# router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^auth/', include(auth_urls)),
    url(r'^profile/', include(profile_urls)),

    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Django Rest Starter'
