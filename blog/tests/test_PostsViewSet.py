from django.urls import reverse
from django.test import tag

from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

from project_user.models import ProjectUser
from blog.models import Post


@tag('PostsViewSet')
class TestPostsViewSet(APITestCase):
    """Test PostsViewSet"""

    def setUp(self):
        self.user = baker.make(ProjectUser)
        self.client.force_authenticate(self.user)

    def test_create_post(self):
        response = self.client.post(
            reverse('blogs'),
            data={
                'text': 'test post'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_posts_list(self):
        baker.make(Post, _quantity=20)
        response = self.client.get(
            reverse('blogs'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 20)
