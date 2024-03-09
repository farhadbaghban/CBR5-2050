from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist, PermissionDenied
from django.db import IntegrityError
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Ad, Comment
from .serializers import (
    AdSerializers,
    CommentSerializers,
)
from .permissions import IsOwnerOrReadOnly


class AdCreateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdSerializers

    def get(self, request, *args, **kwargs):
        if kwargs:
            ad_instance = get_object_or_404(Ad, id=kwargs["pk"])
            serializer = self.serializer_class(instance=ad_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            ads = get_list_or_404(Ad)
            serializer = self.serializer_class(instance=ads, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            try:
                valid_data = ser_data.validated_data
                ad = Ad.objects.create(user=request.user, body=valid_data["body"])
                ser_data = self.serializer_class(instance=ad)
                return Response(ser_data.data, status=status.HTTP_201_CREATED)
            except ValidationError as ex:
                return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdateDeleteView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

    permission_classes = [
        IsOwnerOrReadOnly,
    ]


class AdUpdateDeleteView(ModelViewSet):
    serializer_class = AdSerializers
    queryset = Ad.objects.all()

    permission_classes = [
        IsOwnerOrReadOnly,
    ]
