from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse
import requests
import re

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

@api_view(['POST'])
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
        "redirect_uri": "http://localhost:3000/auth/sign-in",
        "scope": "email profile"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(
        f'https://oauth2.googleapis.com/token?client_id=147097077221-rtgeoqgk09il3n6ibo1hif08hg3vh8mm.apps.googleusercontent.com&client_secret=yMmqoTaM67OIUj4sE3OFmisw&code={code}&grant_type=authorization_code&redirect_uri=http://localhost:3000/auth/sign-in',
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


def checkEmail(email):
    # regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # EMAIL_REG = '/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/'
    EMAIL_REG = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(EMAIL_REG, email):
        return JsonResponse({"msg": "This is a valid email"})


def checkPassword(password):
    PASS_REG = r'[A-Za-z0-9@#$%^&+=]{10,}'
    if re.search(PASS_REG, password):
        return JsonResponse({"msg": "This is a valid password"})


@api_view(['POST'])
def register(request):
    data = request.data

    try:
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = make_password(data['password'])

        EMAIL_REG = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(EMAIL_REG, email) and len(email) >= 10:
            print("Valid Email")
        else:
            message = {'detail': 'This email is invalid'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        PASS_REG = r'[A-Za-z0-9@#$%^&+=]{10,}'
        print(data['password'])
        if re.fullmatch(PASS_REG, data['password']):
            print("Valid password")
        else:
            message = {'detail': 'Password is not valid'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

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

    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


def login(request):
    return JsonResponse({"msg": "Login"})
