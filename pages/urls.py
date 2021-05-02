from django.urls import path
from . import views
from django.contrib import admin
from pages import views

# in charge of connection views to URL.
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2/login', views.google_login, name='oauth2_login'),
    path('', views.home, name='home'),
    path('auth/sign-in', views.google_login_redirect, name = 'oauth2_redirect'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),
    # path('userdata/', views.getLoginCredentials, name="routes")
]