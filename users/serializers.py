from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmationCode

class UserRegisterationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("User already exists!")
        return username


class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()


class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            raise ValidationError({"username": "User not found"})

        if not hasattr(user, 'confirmation_code'):
            raise ValidationError({"code": "No confirmation code found"})

        if user.confirmation_code.code != data['code']:
            raise ValidationError({"code": "Invalid confirmation code"})

        data['user'] = user
        return data
