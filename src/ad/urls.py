from django.urls import path
from .views import (
    AdCreateView,
    CommentCreateView,
    AdUpdateDeleteView,
    CommentUpdateDeleteView,
)

app_name = "ad"


urlpatterns = [
    path("ad/", AdCreateView.as_view(), name="create_list_ads"),
    path("ad/<int:pk>/", AdCreateView.as_view(), name="info_ads"),
    path("comments/<int:pk>/", CommentCreateView.as_view(), name="comment_create_info"),
    path(
        "ad/updel/<int:pk>",
        AdUpdateDeleteView.as_view({"put": "update", "delete": "destroy"}),
        name="ad_delete_update",
    ),
    path(
        "comments/updel/<int:pk>",
        CommentUpdateDeleteView.as_view({"put": "update", "delete": "destroy"}),
        name="comment_delete_update",
    ),
]
