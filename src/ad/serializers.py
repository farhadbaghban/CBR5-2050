from rest_framework import serializers
from .models import Ad, Comment


class AdSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ("body", "id", "user", "comments", "created")
        read_only_fields = ("id", "user", "comments", "created")

    def get_comments(self, obj):
        result = obj.acomments.all()
        return CommentSerializers(instance=result, many=True).data


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "id", "user", "ad", "created")
        read_only_fields = ("id", "user", "ad", "created")
