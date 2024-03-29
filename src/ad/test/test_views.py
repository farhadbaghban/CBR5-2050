from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from accounts.models import User
from ad.models import Ad, Comment


class AdViewTest(APITestCase):
    def setUp(self):
        self.PASSWORD = "123456"
        self.user = User.objects.create_user(
            full_name="farhad baghban fortadest",
            email="baghbanfarhad@foradtest.com",
            password=self.PASSWORD,
        )
        self.user2 = User.objects.create_user(
            full_name="farhad baghban foradtest2",
            email="baghbanfarhad@foradtesttwo.com",
            password=self.PASSWORD,
        )
        self.client = APIClient()
        self.client.login(email=self.user.email, password=self.PASSWORD)
        return super().setUp()

    def test_get_list_ad(self):
        url = reverse("ad:ads-view")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_get_info_ad(self):
        url = reverse("ad:ads-view-detail", args=[1])
        Ad.objects.create(
            user=self.user,
            body="this is body",
        )
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data["body"], "this is body")

    def test_create_ad(self):
        url = reverse("ad:ads-view")
        ad = {
            "body": "this is next body",
        }
        response = self.client.post(url, ad)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
        response = self.client.post(url, ad)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_ad(self):
        self.client.login(email=self.user.email, password=self.PASSWORD)
        Ad.objects.create(
            user=self.user,
            body="this is body",
        )
        url = reverse("ad:ads-view-detail", args=[1])
        update_ad = {"body": "this is updated body"}
        response = self.client.put(url, update_ad)
        self.assertEquals(response.status_code, status.HTTP_200_OK, response.content)
        self.client.logout()
        self.client.login(email=self.user2.email, password=self.PASSWORD)
        response = self.client.put(url, update_ad)
        self.assertEquals(
            response.status_code, status.HTTP_403_FORBIDDEN, response.content
        )

    def test_delete_ad(self):
        self.client.login(email=self.user.email, password=self.PASSWORD)
        Ad.objects.create(
            user=self.user,
            body="this is body",
        )
        url = reverse("ad:ads-view-detail", args=[1])
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentViewTest(APITestCase):
    def setUp(self):
        self.PASSWORD = "123456"
        self.user = User.objects.create_user(
            full_name="farhad baghban forcommenttest",
            email="baghbanfarhad@forcommenttest.com",
            password=self.PASSWORD,
        )
        self.user2 = User.objects.create_user(
            full_name="farhad baghban forcommenttest2",
            email="baghbanfarhad@forcommenttesttwo.com",
            password=self.PASSWORD,
        )
        self.ad = Ad.objects.create(user=self.user, body="this is body")
        self.client = APIClient()
        self.client.login(email=self.user.email, password=self.PASSWORD)
        return super().setUp()

    def test_get_comment(self):
        url = reverse("ad:comment_view", args=[1])
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        Comment.objects.create(
            user=self.user,
            ad=self.ad,
            body="this is comment body",
        )
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.data["body"], "this is comment body", response.content
        )

    def test_create_comment(self):
        url = reverse("ad:comment_view_create")
        comment = {
            "body": "this is next comment body",
            "ad": 1,
        }
        response = self.client.post(url, comment)
        self.assertEquals(
            response.status_code, status.HTTP_201_CREATED, response.json()
        )
        self.client.logout()
        response = self.client.post(url, comment)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_comment(self):
        self.client.login(email=self.user.email, password=self.PASSWORD)
        Comment.objects.create(
            user=self.user,
            ad=self.ad,
            body="this is comment body",
        )
        url = reverse("ad:comment_view", args=[1])
        update_comment = {"body": "this is updated comment body"}
        response = self.client.put(url, update_comment)
        self.assertEquals(response.status_code, status.HTTP_200_OK, response.json())
        self.client.logout()
        self.client.login(email=self.user2.email, password=self.PASSWORD)
        response = self.client.put(url, update_comment)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_comment(self):
        self.client.login(email=self.user.email, password=self.PASSWORD)
        Comment.objects.create(
            user=self.user,
            ad=self.ad,
            body="this is comment body",
        )
        url = reverse("ad:comment_view", args=[1])
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
