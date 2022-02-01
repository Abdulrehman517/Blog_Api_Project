from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='testpassword')
        testuser1.save()

        testpost = Posts.objects.create(
            author=testuser1, title='test post 1',
            body='test body 1'
        )
        testpost.save()

    def test_blog_content(self):
        post = Posts.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'test post 1')
        self.assertEqual(body, 'test body 1')
