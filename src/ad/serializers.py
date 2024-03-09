from rest_framework import serializers
from .models import Ad, Comment


class AdCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("user", "body")


class AdSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ("user", "body", "comments")

    def get_comments(self, obj):
        result = obj.acomments.all()
        return CommentSerializers(instance=result, many=True).data


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "body", "ad")
