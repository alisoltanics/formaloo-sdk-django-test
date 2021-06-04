from django.utils import timezone
from django.conf import settings
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework import status

from .models import Like, Post
from .serializers import PostSerializer
from utils.pagination import CustomPageNumberPagination

from . import constants


class PostsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)
        post.create_formaloo_activity(
            constants.FORMALOO_CREATE_POST_TYPE_ACTIONS_SLUG.get(
                serializer.data.get('type')
            )
        )


class PostViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination

    def get_object(self):
        return generics.get_object_or_404(
            Post,
            uid=self.kwargs.get('uid')
        )

    def like_post(self, serializer, **kwargs):
        post = self.get_object()
        Like.objects.create(
            post=post,
            user=self.request.user
        )
        post.create_formaloo_activity(
            constants.FORMALOO_LIKE_POST_TYPE_ACTIONS_SLUG.get(
                post.type
            )
        )
        return Response(status=status.HTTP_200_OK)
