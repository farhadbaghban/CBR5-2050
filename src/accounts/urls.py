from django.urls import path
from .views import (
    UserListView,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
)


app_name = "accounts"


urlpatterns = [
    path("users/", UserListView.as_view(), name="list_users"),
    path("users/<int:pk>/", UserListView.as_view(), name="user_info"),
    path("users/register/", UserRegisterView.as_view(), name="user_register"),
    path("users/login/", UserLoginView.as_view(), name="user_login"),
    path("users/logout/", UserLogoutView.as_view(), name="user_logout"),
]
