from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ad.views import (
    AdCreateView,
    AdUpdateDeleteView,
    CommentCreateView,
    CommentUpdateDeleteView,
)


class TestUrls(SimpleTestCase):
    def test_list_ads_url_resolves(self):
        url = reverse("ad:create_list_ads")
        self.assertEquals(resolve(url).func.view_class, AdCreateView)

    def test_ad_info_url_resolves(self):
        url = reverse("ad:info_ads", args=[1])
        self.assertEquals(resolve(url).func.view_class, AdCreateView)

    def test_ad_create_url_resolves(self):
        url = reverse("ad:create_list_ads")
        self.assertEquals(resolve(url).func.view_class, AdCreateView)

    def test_ad_update_url_resolves(self):
        url = reverse("ad:ad_delete_update", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"put": "update"}).__name__,
        )

    def test_ad_delete_url_resolves(self):
        url = reverse("ad:ad_delete_update", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            AdUpdateDeleteView.as_view({"delete": "destroy"}).__name__,
        )

    def test_comment_info_url_resolves(self):
        url = reverse("ad:comment_create_info", args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentCreateView)

    def test_comment_create_url_resolves(self):
        url = reverse("ad:comment_create_info", args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentCreateView)

    def test_comment_update_resolves(self):
        url = reverse("ad:comment_delete_update", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            CommentUpdateDeleteView.as_view({"put": "update"}).__name__,
        )

    def test_comment_delete_resolves(self):
        url = reverse("ad:comment_delete_update", kwargs={"pk": 1})
        self.assertEquals(
            resolve(url).func.__name__,
            CommentUpdateDeleteView.as_view({"delete": "destroy"}).__name__,
        )
