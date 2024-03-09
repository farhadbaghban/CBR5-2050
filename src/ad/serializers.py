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

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # If instance exists (update), make 'user' field read-only
            self.fields["user"].read_only = True
            self.fields["user"].required = False


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "id", "user", "ad", "created")
        read_only_fields = ("created", "id")

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ad = serializers.PrimaryKeyRelatedField(queryset=Ad.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # If instance exists (update), make specified field read-only
            for field in ("ad", "user"):
                self.fields[field].read_only = True
                self.fields[field].required = False
