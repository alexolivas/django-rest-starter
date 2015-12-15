from django.conf.urls import url
import views


urlpatterns = [
    url(r'^details/', views.UserDetails.as_view(), name='details'),
    # url(r'^details/(?P<pk>[0-9]+)/$', views.UserDetails.as_view(), name='details'),
    url(r'^preferences/', views.UserPreferencesView.as_view(), name='preferences'),
    url(r'^upload/', views.FileUploadView.as_view(), name='file_upload'),
]
