from rest_framework import serializers
from .models import Ad, Comment


class AdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ad
        field = "__all__"

    def get_answers(self, obj):
        result = obj.acomments.all()
        return CommentSerializers(instance=result, many=True).data


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = "__all__"
