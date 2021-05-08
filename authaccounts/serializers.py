from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'first_name', 'last_name', 'username', 'email']

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        full_name = first_name + last_name
        if first_name == '' or last_name == '':
            full_name=obj.email

        return full_name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)