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
    """
    A ViewSet for handling CRUD operations on comments.

    This ViewSet provides endpoints for creating, updating, retrieving, and deleting comments.

    Attributes:
        serializer_class (CommentSerializers): The serializer class used for serializing and deserializing comment data.
        queryset (Comment.objects.all()): The queryset representing all comments.
        permission_classes (IsOwnerOrReadOnly,): The permission classes applied to this ViewSet.

    Methods:
        create(request, *args, **kwargs): Handles HTTP POST requests for creating a new comment.
        retrieve(request, *args, **kwargs): Handles HTTP GET requests for retrieving a comment by its ID.
        update(request, *args, **kwargs): Handles HTTP PUT requests for updating an existing comment.
        destroy(request, *args, **kwargs): Handles HTTP DELETE requests for deleting an existing comment.
    """

    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

    permission_classes = [
        IsOwnerOrReadOnly,
    ]


class AdUpdateDeleteView(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on Ads.

    This ViewSet provides endpoints for creating, updating, retrieving, and deleting Ads.

    Attributes:
        serializer_class (AdSerializers): The serializer class used for serializing and deserializing Ad data.
        queryset (Ad.objects.all()): The queryset representing all Ads.
        permission_classes (IsOwnerOrReadOnly,): The permission classes applied to this ViewSet.

    Methods:
        create(request, *args, **kwargs): Handles HTTP POST requests for creating a new Ad.
        retrieve(request, *args, **kwargs): Handles HTTP GET requests for retrieving a Ad by its ID.
        list(request, *args, **kwargs): Handles HTTP GET requests for Listing Ads with another url.
        update(request, *args, **kwargs): Handles HTTP PUT requests for updating an existing Ad.
        destroy(request, *args, **kwargs): Handles HTTP DELETE requests for deleting an existing Ad.
    """

    serializer_class = AdSerializers
    queryset = Ad.objects.all()

    permission_classes = [
        IsOwnerOrReadOnly,
    ]
