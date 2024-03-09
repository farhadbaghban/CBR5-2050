from django.urls import path
from .views import (
    AdCreateView,
    AdUpdateDeleteView,
    CommentUpdateDeleteView,
)

app_name = "ad"


urlpatterns = [
    path(
        "ad/",
        AdUpdateDeleteView.as_view({"get": "list", "post": "create"}),
        name="ads-view",
    ),
    path(
        "ad/<int:pk>/",
        AdUpdateDeleteView.as_view(
            {"put": "update", "delete": "destroy", "get": "retrieve"}
        ),
        name="ads-view-detail",
    ),
    path(
        "comments/",
        CommentUpdateDeleteView.as_view(
            {
                "post": "create",
            }
        ),
        name="comment_view_create",
    ),
    path(
        "comments/<int:pk>",
        CommentUpdateDeleteView.as_view(
            {
                "put": "update",
                "delete": "destroy",
                "get": "retrieve",
            }
        ),
        name="comment_view",
    ),
]
