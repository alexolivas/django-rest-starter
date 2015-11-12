from django.conf.urls import url
from djangorest.apps.accounts import views


# Login is handled by curl -X POST http://localhost:8000/api-token-auth/ -d "password=admin&username=admin"??
# This should not be handled by that because I need to return the user object
urlpatterns = [
    url(r'^edit/', views.EditProfileView.as_view(), name='edit-user'),
    url(r'^create/', views.CreateUserView.as_view(), name='create-user'),
    url(r'^manage/', views.EditUserView.as_view(), name='manage-user'),
    url(r'^delete/', views.DeleteUserView.as_view(), name='delete-user'),
]

