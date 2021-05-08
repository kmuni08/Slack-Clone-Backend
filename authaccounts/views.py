from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse
import requests

from rest_framework import status

# from django.contrib.auth.models import User
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, UserSerializerWithToken
from django.contrib.auth.hashers import make_password


# Create methods and link urls to methods.

# Create your views here. Render/return data to the webpage itself by returning JSON.

# auth_url_google = "https://accounts.google.com/o/oauth2/v2/auth?client_id=147097077221-rtgeoqgk09il3n6ibo1hif08hg3vh8mm.apps.googleusercontent.com&redirect_uri=http://localhost:8000/auth/sign-in&response_type=code&scope=email profile"

def home(request: HttpRequest):
    return JsonResponse({"msg": "Hello World"})


# login route for social.
# def social_login(request: HttpRequest):
#     return redirect(auth_url_google)

def google_sign_in(request: HttpRequest):
    code = request.GET.get('code')
    print("code", code)
    user = exchange_code(code)
    # exchange_code(code)
    # return JsonResponse({"msg": "Redirected"})
    return JsonResponse({"user": user})


def exchange_code(code: str):
    data = {
        "client_id": "147097077221-rtgeoqgk09il3n6ibo1hif08hg3vh8mm.apps.googleusercontent.com",
        "client_secret": "yMmqoTaM67OIUj4sE3OFmisw",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/auth/sign-in",
        "scope": "email profile"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(
        "https://oauth2.googleapis.com/token?client_id=147097077221-rtgeoqgk09il3n6ibo1hif08hg3vh8mm.apps.googleusercontent.com&client_secret=yMmqoTaM67OIUj4sE3OFmisw&code=4%2F0AY0e-g7yiKBRb6rUAmeTfMp7aRVSPDyKWgMZmIcCELP9zlpUs7OO-zfmUBMTtifgGjUISg&grant_type=authorization_code&redirect_uri=http://localhost:8000/auth/sign-in",
        data=data, headers=headers)
    print(response)
    credentials = response.json()
    print("CREDENTIALS ", credentials)
    print("access token ", credentials['access_token'])
    access_token = credentials['access_token']
    # print("access token ", access_token)
    response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print("response", response)
    user = response.json()
    print("user", user)
    return user


# --------------------------------------------------------------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    data = request.data

    try:
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = make_password(data['password'])

        user = User(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        # return token
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

        # if User.filter(username=username).exists():
        #     return JsonResponse({"msg": "Username exists"})
        # else:
        #     if User.objects.filter(email=email).exists():
        #         return JsonResponse({"msg": "Email exists"})
        #     else:

    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


def login(request):
    return JsonResponse({"msg": "Login"})