from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import (
    UserRegisterationSerializer,
    UserAuthorizationSerializer,
    UserConfirmSerializer
)
from .models import ConfirmationCode


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(username=username, password=password)
    user.is_active = False
    user.save()

    code = ConfirmationCode.generate_code()
    ConfirmationCode.objects.create(user=user, code=code)

    
    print(f"Confirmation code for {username}: {code}")

    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id, 'message': 'User registered. Please confirm your account.'})


@api_view(['POST'])
def confirmation_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']
    user.is_active = True
    user.save()

    user.confirmation_code.delete()

    return Response({"message": "Account confirmed successfully!"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(data={'error': 'User credentials are wrong!'},
                    status=status.HTTP_401_UNAUTHORIZED)
