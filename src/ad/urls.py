from django.urls import path
from .views import (
    AdCreateView,
    AdListView,
    CommentListView,
    CommentCreateView,
    AdUpdateDeleteView,
    CommentUpdateDeleteView,
)

app_name = "ad"


urlpatterns = [
    path("ads/", AdListView.as_view(), name="list_ads"),
    path("ads/<int:pk>/", AdListView.as_view(), name="ad_info"),
    path("ads/create/", AdCreateView.as_view(), name="ad_create"),
    path("comments/<int:pk>/", CommentListView.as_view(), name="comment_info"),
    path(
        "comments/create/<int:pk>", CommentCreateView.as_view(), name="comment_create"
    ),
    path(
        "ads/update/<int:pk>",
        AdUpdateDeleteView.as_view({"put": "update"}),
        name="ad_update",
    ),
    path(
        "ads/delete/<int:pk>",
        AdUpdateDeleteView.as_view({"delete": "destroy"}),
        name="ad_delete",
    ),
    path(
        "comments/update/<int:pk>",
        CommentUpdateDeleteView.as_view({"put": "update"}),
        name="comment_update",
    ),
    path(
        "comments/delete/<int:pk>",
        CommentUpdateDeleteView.as_view({"delete": "destroy"}),
        name="comment_delete",
    ),
]
