# Create your tests here.
import email
from turtle import title
from typing_extensions import Self
from django.test import TestCase,client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class BlogTests (TestCase) :
    def setUp(self) :
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password= 'secret'
        )
        self.Post = Post.objects.create(
            title = 'A good title',
            author = self.user,
            body = 'Nice body content'
        )
    def test_string_representation(self):
        post = post(title = 'a sampletest')
        self.assertEqual(str(post),post.title)
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')