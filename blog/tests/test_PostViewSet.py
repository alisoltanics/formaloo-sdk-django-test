from django.urls import reverse
from django.test import tag

from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

from project_user.models import ProjectUser
from blog.models import Like, Post


@tag('PostViewSet')
class TestPostViewSet(APITestCase):
    """Test PostViewSet"""

    def setUp(self):
        self.user = baker.make(ProjectUser)
        self.client.force_authenticate(self.user)
        self.post = baker.make(Post)

    def test_get_post(self):
        response = self.client.get(
            reverse('get-post', kwargs={'uid': self.post.uid})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_post(self):
        response = self.client.post(
            reverse('like-post', kwargs={'uid': self.post.uid}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.all().count(), 1)
