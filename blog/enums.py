from django.db.models import enums


class PostType(enums.TextChoices):
    TEXT = 'text', "Text"
    IMAGE = 'image', "Image"
    SONG = 'song', "Song"
