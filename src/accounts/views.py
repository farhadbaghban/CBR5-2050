from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from .models import User
from .serializers import (
    UserRegisterSerializer,
    UserListSerializer,
    UserLoginSerializer,
)


class UserListView(APIView):
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs:
            user_instance = get_object_or_404(User, id=kwargs["pk"])
            serializer = self.serializer_class(user_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            users = get_list_or_404(User)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [
        AllowAny,
    ]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response("You are authenticated", status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [
        AllowAny,
    ]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response("you are loged in", status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            valid_data = ser_data.validated_data
            user = authenticate(
                request,
                email=valid_data["email"],
                password=valid_data["password"],
            )

            if user is not None:
                login(request, user)
                return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
            return Response(ser_data.data, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)
