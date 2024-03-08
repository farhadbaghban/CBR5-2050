from django.db import models
from accounts.models import User


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ucomments")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="acomments")
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "ad"], name="unique_user_ad")
        ]

    def __str__(self):
        return f"{self.user}  -  {self.body[:30]}"
