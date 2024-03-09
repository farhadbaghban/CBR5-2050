from django.db import models
from accounts.models import User


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = [
            "body",
        ]

    def __str__(self):
        return self.body


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ucomments")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="acomments")
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "ad"], name="unique_user_ad")
        ]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = [
            "body",
        ]

    def __str__(self):
        return f"{self.user}  -  {self.body[:30]}"
