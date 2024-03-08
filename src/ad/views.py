from django.core.exceptions import ValidationError, ObjectDoesNotExist, PermissionDenied
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, I
from models import Ad, Comment
from serializers import AdSerializers, CommentSerializers
from permissions import IsOwnerOrReadOnly


class AdCreateListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdSerializers

    def post(self, request, *args, **kwargs):
        ser_data = self.serializer_class(request.POST)
        if ser_data.is_valid():
            try:
                valid_data = ser_data.validated_data
                ad = Ad.objects.create(
                    user=request.user, body=valid_data["body"], slug=valid_data["slug"]
                )
                ser_data = self.serializer_class(instance=ad)
                return Response(ser_data.data, status=status.HTTP_201_CREATED)
            except ValidationError as ex:
                return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentCreateListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdSerializers

    def post(self, request, *args, **kwargs):
        ser_data = self.serializer_class(request.POST)
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


class AdUpdateDeleteView(APIView):
    serializer_class = AdSerializers

    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def dispatch(self, request, *args, **kwargs):
        try:
            self.ad_instance = Ad.objects.get(id=kwargs["pk"])
            self.check_object_permissions(request, self.ad_instance)
        except PermissionDenied as ex:
            return Response(ex.error_dict, status=status.HTTP_403_FORBIDDEN)
        except IntegrityError as ex:
            return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)

        return super().dispatch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ser_data = self.serializer_class(
            instance=self.ad_instance, data=request.POST, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.ad_instance.delete()
        return Response({"message": "Ad deleted"}, status=status.HTTP_200_OK)


class CommentUpdateDeleteView(APIView):
    serializer_class = CommentSerializers

    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def dispatch(self, request, *args, **kwargs):
        try:
            self.comment_instance = Comment.objects.get(id=kwargs["pk"])
            self.check_object_permissions(request, self.comment_instance)
        except PermissionDenied as ex:
            return Response(ex.error_dict, status=status.HTTP_403_FORBIDDEN)
        except IntegrityError as ex:
            return Response(ex.error_dict, status=status.HTTP_400_BAD_REQUEST)

        return super().dispatch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ser_data = self.serializer_class(
            instance=self.comment_instance, data=request.POST, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.comment_instance.delete()
        return Response({"message": "Ad deleted"}, status=status.HTTP_200_OK)
