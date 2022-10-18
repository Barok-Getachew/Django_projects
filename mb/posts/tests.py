# Create your tests here.
from django.test import TestCase
from .models import post
from django.urls import reverse

class PostModelTest(TestCase) :
    def setUp(self) -> None:
        post.objects.create(text="just a test") 
    def test_text_content(self) :
        Post = post.objects.get(id=1)
        expected_object_name  =f'{Post.text}'
        self.assertEqual(expected_object_name, 'just a test')
class HomePageViewTest(TestCase):
    def setUp(self):
        post.objects.create(text='this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('old/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')        