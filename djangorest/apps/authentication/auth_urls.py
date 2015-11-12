from django.conf.urls import url

from djangorest.apps.authentication import views



# Login is handled by curl -X POST http://localhost:8000/api-token-auth/ -d "password=admin&username=admin"??
# This should not be handled by that because I need to return the user object
urlpatterns = [
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    # url(r'^create/user/', views.CreateAccountView.as_view(), name='create'),
    # url(r'^delete/user/', views.UpdateAccountView.as_view(), name='update'),
]
