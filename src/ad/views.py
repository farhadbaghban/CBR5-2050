from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist, PermissionDenied
from django.db import IntegrityError
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Ad, Comment
from .serializers import (
    AdSerializers,
    CommentSerializers,
    AdCreateSerializers,
)
from .permissions import IsOwnerOrReadOnly


class AdListView(APIView):
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


class CommentListView(APIView):
    serializer_class = CommentSerializers

    def get(self, request, *args, **kwargs):
        comment_instance = get_object_or_404(Comment, id=kwargs["pk"])
        serializer = self.serializer_class(instance=comment_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdCreateSerializers

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


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializers

    def post(self, request, *args, **kwargs):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            try:
                ad = Ad.objects.get(id=kwargs["pk"])
                valid_data = ser_data.validated_data
                comment = Comment.objects.create(
                    user=request.user, ad=ad, body=valid_data["body"]
                )
                return Response(ser_data.data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist as ex:
                return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)
            except IntegrityError as ex:
                return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)
            except ValidationError as ex:
                return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdateDeleteView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet
):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

    permission_classes = [
        IsOwnerOrReadOnly,
    ]


# class CommentUpdateDeleteView(APIView):
#     serializer_class = CommentSerializers

#     permission_classes = [
#         IsOwnerOrReadOnly,
#     ]

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             self.comment_instance = Comment.objects.get(id=kwargs["pk"])
#             self.check_object_permissions(request, self.comment_instance)
#         except PermissionDenied as ex:
#             return Response(ex.error_dict, status=status.HTTP_403_FORBIDDEN)
#         except IntegrityError as ex:
#             return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)

#         return super().dispatch(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         ser_data = self.serializer_class(
#             instance=self.comment_instance, data=request.POST, partial=True
#         )
#         if ser_data.is_valid():
#             ser_data.save()
#             self.comment_instance.updated = datetime.now()
#             return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
#         return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         self.comment_instance.delete()
#         return Response({"message": "Ad deleted"}, status=status.HTTP_200_OK)


class AdUpdateDeleteView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet
):
    serializer_class = AdSerializers
    queryset = Ad.objects.all()

    permission_classes = [
        IsOwnerOrReadOnly,
    ]
