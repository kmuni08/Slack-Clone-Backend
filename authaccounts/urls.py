from django.urls import path
from . import views
from django.contrib import admin

# in charge of connection views to URL.
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('auth/social-sign-in', views.google_sign_in, name='oauth2_sign_in')
]
