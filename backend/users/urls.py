from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from backend.users import views
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'create_company', views.CompanyViewSet)

urlpatterns = [
    url(r'^auth/obtain_token/$', obtain_jwt_token),
    url(r'^auth/refresh_token/$', refresh_jwt_token),
    url(r'^create_users/$', views.create_user, name='createUser'),
    url(r'^create_company/$', views.create_company, name='createCompany'),
    url(r'^register/$', views.UserRegistration.as_view(), name='submit&showscreen1'),
    url(r'^display_all_users/$', views.DisplayAllUsersView.as_view(), name='displayAllUsers'),
    url(r'^display_companies/$', views.DisplayCompanyView.as_view(), name='displayCompany'),
    url(r'^display_all_user_profile/$', views.DisplayUserProfileView.as_view(), name='displayAllUserProfie'),
    url(r'^display_user_profile_for_web/$', views.DisplayUserProfileForWebView.as_view(), name='displayUserProfile'),
    url(r'^display_user_in_company/$', views.DisplayUserInCompany.as_view(), name='userInCompany'),
    url(r'display_screen1/$', views.DisplayScreen1View.as_view(), name='displayScreen1'),
    url(r'display_screen2/$', views.DisplayScreen2View.as_view(), name='displayScreen2'),
    url(r'display_screen3/$', views.DisplayScreen3View.as_view(), name='displayScreen3'),
    url(r'display_screen4/$', views.DisplayScreen4View.as_view(), name='displayScreen4'),
    url(r'display_screen5/$', views.DisplayScreen5View.as_view(), name='displayScreen5'),
    url(r'^submit_screen2/$', views.SubmitScreen2View.as_view(), name='submitScreen2'),
    url(r'^submit_screen3/$', views.SubmitScreen3View.as_view(), name='submitScreen3'),
    url(r'^submit_screen4/$', views.SubmitScreen4View.as_view(), name='submitScreen4'),
    url(r'^submit_screen5/$', views.SubmitScreen5View.as_view(), name='submitScreen5'),
    url(r'^testing/$', views.TestingUserInCompany.as_view(), name='tesing')
]
