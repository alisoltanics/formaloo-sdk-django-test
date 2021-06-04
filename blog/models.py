from django.db import models
from django.utils import timezone

from utils.base_model import BaseModel
from project_user.models import ProjectUser
from .enums import PostType

from formaloo.activities.activity import Activity


class Post(BaseModel):
    """Data model for Post."""

    user = models.ForeignKey(
        ProjectUser, on_delete=models.PROTECT,
        verbose_name="User",
        related_name='posts'
    )

    type = models.CharField(
        "Type",
        max_length=10,
        null=True,
        blank=True,
        choices=PostType.choices,
        default=PostType.TEXT,
    )

    text = models.CharField(
        verbose_name="Text",
        max_length=1500,
        null=True, blank=True,
    )

    song_url = models.CharField(
        verbose_name="Song",
        max_length=250,
        null=True, blank=True,
        help_text='Add song url'
    )

    image_url = models.CharField(
        verbose_name="Image",
        max_length=250,
        null=True, blank=True,
        help_text='Add image url'
    )

    def create_formaloo_activity(self, action_slug):
        activity = Activity(
            action={
                "slug": action_slug
            },
            customer_data={
                "code": self.user_id
            },
            activity_date=timezone.now().isoformat()
        )
        activity.create()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created",)

    def __str__(self):
        return str(self.id)


class Like(BaseModel):
    """Data model for Like."""

    user = models.ForeignKey(
        ProjectUser, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="User",
        related_name='likes'
    )

    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Post",
        related_name='likes'
    )

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ("-created",)

    def __str__(self):
        return str(self.id)
