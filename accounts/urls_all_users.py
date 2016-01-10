from django.conf.urls import url
import views_user


urlpatterns = [
    url(r'^$', views_user.MyProfile.as_view(), name='details'),
    url(r'^(?P<pk>[0-9]+)/$', views_user.UserDetails.as_view(), name='user-details'),
    url(r'^preferences/', views_user.UserPreferencesView.as_view(), name='preferences'),
    url(r'^upload/', views_user.FileUploadView.as_view(), name='file_upload'),
]
