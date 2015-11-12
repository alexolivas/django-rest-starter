"""djangorest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from djangorest.apps.authentication import auth_urls
from djangorest.apps.users import user_urls

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/auth/', include(auth_urls)),
    url(r'^v1/users/', include(user_urls)),
    # url(r'^api-token-auth/', views.obtain_auth_token), # Automatically gets or generates new token
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Gives Login Access to the Webapp
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Django REST Skeleton Administration'
