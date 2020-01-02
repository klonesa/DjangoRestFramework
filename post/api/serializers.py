from rest_framework import serializers

from post.models import Post


class PostSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    username = serializers.SerializerMethodField(method_name='username_new')

    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'image',
            'url',
            'created',
            'modified_by'
        ]

    def username_new(self, obj):
        return str(obj.user.username)


class PostUpdateCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]
