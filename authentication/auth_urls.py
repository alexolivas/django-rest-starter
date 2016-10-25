from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
]
