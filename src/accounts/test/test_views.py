import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from accounts.models import User
from accounts.serializers import (
    UserListSerializer,
    UserRegisterSerializer,
    UserLoginSerializer,
)


class UserViewTest(APITestCase):
    def setUp(self):
        User.objects.bulk_create(
            [
                User(
                    full_name="farhad test" + str(i * ("a")),
                    email="farhad" + str(i * ("a")) + "@email.com",
                )
                for i in range(24)
            ]
        )
        self.client = APIClient()
        return super().setUp()

    def test_list_all_active_user(self):
        url = reverse("accounts:list_users")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(User.objects.count(), 24)

    def test_one_user_info(self):
        user = User.objects.first()
        url = reverse("accounts:user_info", kwargs={"pk": user.pk})
        response = self.client.get(url)
        ser_data = UserListSerializer(instance=user).data
        response_data = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data, ser_data)


class UserRegisterTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("accounts:user_register")
        self.registerdata = {
            "full_name": "farhad baghbann",
            "email": "baghbanfarhad@email.com",
            "password": "123456",
        }
        return super().setUp()

    def test_user_registeration(self):
        response = self.client.post(self.url, self.registerdata)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class UserAuthenticationTest(APITestCase):
    def setUp(self):
        PASSWORD = "123456"
        valid_user = User.objects.create_user(
            full_name="farhad baghbann",
            email="baghbanfarhad@email.com",
            password=PASSWORD,
        )
        self.authentication_true = {
            "email": valid_user.email,
            "password": PASSWORD,
        }
        self.authentication_False = {
            "email": valid_user.email,
            "password": "123455",
        }
        self.authentication_bade_request = {}
        self.serializer_class = UserLoginSerializer
        self.client = APIClient()
        return super().setUp()

    def test_user_authentication(self):
        url = reverse("accounts:user_login")
        response_False = self.client.post(url, self.authentication_False)
        response_bad_request = self.client.post(url, self.authentication_bade_request)
        response_true = self.client.post(url, self.authentication_true)

        self.assertEquals(response_False.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(response_bad_request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response_true.status_code, status.HTTP_202_ACCEPTED)

    def test_user_logout(self):
        url = reverse("accounts:user_logout")
        self.client.login(email="baghbanfarhad@email.com", password="123456")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
