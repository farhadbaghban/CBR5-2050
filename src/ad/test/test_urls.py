from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ad.views import (
    AdUpdateDeleteView,
    CommentUpdateDeleteView,
)


class TestUrls(SimpleTestCase):
    def test_list_ads_url_resolves(self):
        url = reverse("ad:ads-view")
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"get": "list"}).__name__,
        )

    def test_ad_info_url_resolves(self):
        url = reverse("ad:ads-view-detail", args=[1])
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"get": "retrieve"}).__name__,
        )

    def test_ad_create_url_resolves(self):
        url = reverse("ad:ads-view")
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"post": "create"}).__name__,
        )

    def test_ad_update_url_resolves(self):
        url = reverse("ad:ads-view-detail", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"put": "update"}).__name__,
        )

    def test_ad_delete_url_resolves(self):
        url = reverse("ad:ads-view-detail", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"delete": "destroy"}).__name__,
        )

    def test_comment_info_url_resolves(self):
        url = reverse("ad:comment_view", args=[1])
        self.assertEquals(
            resolve(url).func.__name__,
            CommentUpdateDeleteView.as_view({"get": "retrieve"}).__name__,
        )

    def test_comment_create_url_resolves(self):
        url = reverse("ad:comment_view_create")
        self.assertEquals(
            resolve(url).func.__name__,
            CommentUpdateDeleteView.as_view({"post": "create"}).__name__,
        )

    def test_comment_update_resolves(self):
        url = reverse("ad:comment_view", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            CommentUpdateDeleteView.as_view({"put": "update"}).__name__,
        )

    def test_comment_delete_resolves(self):
        url = reverse("ad:comment_view", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            CommentUpdateDeleteView.as_view({"delete": "destroy"}).__name__,
        )
