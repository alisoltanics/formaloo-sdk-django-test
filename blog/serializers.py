from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serialize Post model data."""

    class Meta:
        model = Post
        fields = (
            'uid', 'text',
            'song_url', 'image_url',
            'type', 'created', 'updated'
        )
        read_only_fields = ('uid', 'created', 'updated')
