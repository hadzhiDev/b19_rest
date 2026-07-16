from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import serializers


from .serializers import (
    LoginSerializer, RegisterSerializer,
    ProfileSerializer, ChangePasswordSerializer,
    DeactivateSerializer
)


@api_view(["POST"])
@permission_classes([AllowAny])
def custom_login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.validated_data)


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary='Регистрация нового пользователя',
    operation_description='Регистрация нового пользователя',
))
@api_view(["POST"])
def custom_register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == "GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    if request.method in ["PUT", "PATCH"]:
        serializer = ProfileSerializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request: Request):
    serializer = ChangePasswordSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"detail": "Пароль успешно изменен."})
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request: Request):
    user = request.user
    Token.objects.filter(user=user).delete()
    return Response(
        {"detail": "Вы успешно вышли из системы."}, 
        status=status.HTTP_200_OK
    )

@api_view(["POST"])
def deactivate(request):
    serializer = DeactivateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    if not serializer.validated_data['confirm']:
        raise serializers.ValidationError("Подтвердите деактивацию аккаунта")
    
    user = request.user
    user.is_active = False
    user.save()
    return Response(
        {"detail": "Ваш аккаунт был деактивирован."},
        status=status.HTTP_200_OK
    )