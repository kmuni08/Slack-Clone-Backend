from django.urls import path
from . import views

# in charge of connection views to URL.
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),
    path('userdata/', views.getLoginCredentials, name="routes")
]