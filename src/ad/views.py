from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Ad, Comment
from .serializers import (
    AdSerializers,
    CommentSerializers,
)
from .permissions import IsOwnerOrReadOnly


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
