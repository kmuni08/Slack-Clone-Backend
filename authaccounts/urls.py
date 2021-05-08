from django.urls import path
from . import views
from django.contrib import admin

# in charge of connection views to URL.
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    # path('oauth2/login', views.social_login, name='oauth2_login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('auth/sign-in', views.google_sign_in, name='oauth2_sign_in')
]