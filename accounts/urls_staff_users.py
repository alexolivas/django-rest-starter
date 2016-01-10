from django.conf.urls import url
import views_users_list


urlpatterns = [
    url(r'^$', views_users_list.UserSearch.as_view(), name='search'),
]

