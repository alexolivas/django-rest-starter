from django.conf.urls import url
import views
# from apps.authentication import views


# url(r'^profile/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view(), name='profile'),
urlpatterns = [
    # url(r'^logindetails/', views.UserLoginDetails.as_view(), name='login_details'),
    url(r'^details/', views.UserAccountDetails.as_view(), name='details'),
]
