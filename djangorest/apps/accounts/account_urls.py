from django.conf.urls import url
from djangorest.apps.accounts import views

# TODO Change these to the real account views i.e. user_views, account_views
# TODO What I am working on here is only needed for the CELLA project i.e. adding user_views, user_urls etc
urlpatterns = [
    url(r'^edit/', views.EditProfileView.as_view(), name='edit-account'),
    url(r'^create/', views.CreateUserView.as_view(), name='create-account'),
    url(r'^manage/', views.EditUserView.as_view(), name='manage-account'),
    url(r'^delete/', views.DeleteUserView.as_view(), name='delete-account'),
]

