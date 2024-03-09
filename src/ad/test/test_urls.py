from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ad.views import (
    AdListView,
    AdCreateView,
    AdUpdateDeleteView,
    CommentListView,
    CommentCreateView,
    CommentUpdateDeleteView,
)


class TestUrls(SimpleTestCase):
    def test_list_ads_url_resolves(self):
        url = reverse("ad:list_ads")
        self.assertEquals(resolve(url).func.view_class, AdListView)

    def test_ad_info_url_resolves(self):
        url = reverse("ad:ad_info", args=[1])
        self.assertEquals(resolve(url).func.view_class, AdListView)

    def test_ad_create_url_resolves(self):
        url = reverse("ad:ad_create")
        self.assertEquals(resolve(url).func.view_class, AdCreateView)

    def test_ad_update_resolves(self):
        url = reverse("ad:ad_update", args=[1])
        self.assertEquals(resolve(url).func.view_class, AdUpdateDeleteView)

    def test_ad_delete_resolves(self):
        url = reverse("ad:ad_delete", args=[1])
        self.assertEquals(resolve(url).func.view_class, AdUpdateDeleteView)

    def test_comment_info_url_resolves(self):
        url = reverse("ad:comment_info", args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentListView)

    def test_comment_create_url_resolves(self):
        url = reverse("ad:comment_create")
        self.assertEquals(resolve(url).func.view_class, CommentCreateView)

    def test_comment_update_resolves(self):
        url = reverse("ad:comment_update", args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentUpdateDeleteView)

    def test_comment_delete_resolves(self):
        url = reverse("ad:comment_delete", args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentUpdateDeleteView)
