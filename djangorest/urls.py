from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from authentication import auth_urls

schema_view = get_swagger_view(title='Django Rest Skeleton API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', schema_view),
    url(r'^v1/auth/', include(auth_urls)),

    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Django Rest Skeleton'
