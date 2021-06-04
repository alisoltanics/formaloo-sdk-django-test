from django.urls import path

from . import views


urlpatterns = [
    path(
        'posts',
        views.PostsViewSet.as_view(
            {
                'get': 'list',
                'post': 'create'
            }
        ), name='blogs'
    ),
    path(
        'posts/<str:uid>/like-post',
        views.PostViewSet.as_view(
            {
                'post': 'like_post'
            }
        ),
        name='like-post'
    ),
    path(
        'posts/<str:uid>',
        views.PostViewSet.as_view(
            {
                'get': 'retrieve'
            }
        ),
        name='get-post'
    ),
]
